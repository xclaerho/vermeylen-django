from django.contrib import admin
from .models import Activity
# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name','description','location','price']}),
        ('Datum', {'fields':['start','end']}),
        ('Socials', {'fields':['facebooklink','addtocalendar','googlecalendarlink','googlecalendarid']}),
        ('Afbeelding', {'fields':['image']})
    ]
    list_display = ('name', 'start')
    list_filter = ['start']
    search_fields = ['name']
    readonly_fields = ['googlecalendarlink','googlecalendarid']

    # only praeses can add events to the calendar
    def add_view(self, request, form_url='', extra_context=None):
        if not request.user.has_perm('activities.add_to_calendar'):
            self.readonly_fields = ['googlecalendarlink','googlecalendarid','addtocalendar']
        else:
            self.readonly_fields = ['googlecalendarlink','googlecalendarid']
        return super(ActivityAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not request.user.has_perm('activities.add_to_calendar'):
            self.readonly_fields = ['googlecalendarlink','googlecalendarid','addtocalendar']
        else:
            self.readonly_fields = ['googlecalendarlink','googlecalendarid']
        return super(ActivityAdmin, self).change_view(request, object_id, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        if request.user.has_perm('activities.add_to_calendar'):
            self.list_display = ('name','start','addtocalendar')
            self.list_filter = ['start','addtocalendar']
        else:
            self.list_display = ('name','start')
            self.list_filter = ['start']
        return super(ActivityAdmin, self).changelist_view(request, extra_context)

admin.site.register(Activity, ActivityAdmin)