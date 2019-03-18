from django.db import models
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

class Activity(models.Model):
    name = models.CharField(max_length=50,verbose_name="naam")
    start = models.DateTimeField()
    end = models.DateTimeField(verbose_name="einde")
    description = models.TextField(blank=True,null=True,verbose_name="beschrijving")
    location = models.CharField(blank=True,null=True,max_length=50,verbose_name="locatie")
    price = models.FloatField(blank=False,null=False,default=0,verbose_name="prijs")
    image = models.ImageField(blank=True,null=True,upload_to="acitivity_images",verbose_name="Afbeelding")
    facebooklink = models.URLField(max_length = 500, blank=True,null=True,verbose_name="Facebook link")
    addtocalendar = models.BooleanField(verbose_name='toegevoegd aan Google calendar?',default=False,help_text='Door praeses aan te klikken wanneer het aan de calendar toegevoegd mag worden.')
    googlecalendarlink = models.URLField(max_length = 500, blank=True,null=True,verbose_name="Google calendar link")
    googlecalendarid = models.CharField(max_length=100,blank=True,null=True,verbose_name="ID van activiteit op Google calendar")

    def __str__(self):
        return self.name + ", " + str(self.start)

    def save(self, *args, **kwargs):
        # check if needs to be added/updated to calendar
        if self.addtocalendar is True:
            # check if already in calendar (and update if it is)
            if self.googlecalendarid is not None:
                calendarUpdate(self)
            elif self.addtocalendar is True:
                calendarInfo = calendarInsert(self)
                self.googlecalendarlink = calendarInfo.get('htmlLink')
                self.googlecalendarid = calendarInfo.get('eventId')
        super(Activity, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "activiteit"
        verbose_name_plural = "activiteiten"
        ordering = ['-start']
        permissions = (
            ("add_to_calendar", "Can add events to Google calendar"),
        )

# Everything related to Google calendar
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

def calendarInsert(event):
    # credentials if not provided
    store = file.Storage(os.path.join(os.path.dirname(__file__),'auth_files/token.json'))
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(os.path.join(os.path.dirname(__file__),'auth_files/credentials.json'), SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # create event
    cal_event = {
    'summary': event.name,
    'location': event.location,
    'description': event.description,
    'start': {
        'dateTime': event.start.isoformat(),
        'timeZone': 'Europe/Brussels',
    },
    'end': {
        'dateTime': event.end.isoformat(),
        'timeZone': 'Europe/Brussels',
    }
    }

    # insert in calendar and return necessary attributes
    cal_event = service.events().insert(calendarId='primary', body=cal_event).execute()
    return {'htmlLink': cal_event.get('htmlLink'), 'eventId': cal_event.get('id')}

def calendarUpdate(event):
    # only update the google calendar if it's on there
    if event.googlecalendarid is not None:
        # credentials if not provided
        store = file.Storage(os.path.join(os.path.dirname(__file__),'auth_files/token.json'))
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(os.path.join(os.path.dirname(__file__),'auth_files/credentials.json'), SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('calendar', 'v3', http=creds.authorize(Http()))

        # First retrieve the event from the API.
        cal_event = service.events().get(calendarId='primary', eventId=event.googlecalendarid).execute()

        # Update fields
        cal_event['summary'] = event.name
        cal_event['location'] = event.location
        cal_event['description'] = event.description
        cal_event['start']['dateTime'] = event.start.isoformat()
        cal_event['end']['dateTime'] = event.end.isoformat()

        # Update online
        service.events().update(calendarId='primary', eventId=cal_event['id'], body=cal_event).execute()

@receiver(pre_delete, sender=Activity)
def calendarDelete(sender, instance, **kwargs):
    if instance.googlecalendarid is not None:
        # credentials if not provided
        store = file.Storage(os.path.join(os.path.dirname(__file__),'auth_files/token.json'))
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(os.path.join(os.path.dirname(__file__),'auth_files/credentials.json'), SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('calendar', 'v3', http=creds.authorize(Http()))

        # Execute delete
        try:
            service.events().delete(calendarId='primary', eventId=instance.googlecalendarid).execute()
        except:
            # catch HttpError thrown when event is already deleted from the calendar
            pass
