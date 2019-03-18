from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

class Person(models.Model):
    name = models.CharField(max_length=50,verbose_name="naam")
    club = models.CharField(max_length=50, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True) # null needs to be true for set null to work

    def __str__(self):
        return self.name + " (" + self.club + ")"
    
    class Meta:
        verbose_name = "persoon"
        verbose_name_plural = "personen"
        permissions = (
            ("view_muilgraaf", "Can see muilgraaf when logged in"),
        )
    
class Link(models.Model):
    TYPES = (
        (0, 'Muilen'),
        (1, 'Sex'),
        (2, 'Relatie')
    )
    pid = models.ForeignKey(Person,on_delete=models.CASCADE,related_name='first_person', verbose_name='Persoon 1')
    sid = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='second_person',verbose_name='Persoon 2')
    link_type = models.IntegerField(choices=TYPES, default=0)
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True) 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.pid) + " en " + str(self.sid)

    def clean(self):
        if self.pid==self.sid:
            raise ValidationError({'sid':'Persoon 1 en 2 moeten verschillend zijn.'})
    