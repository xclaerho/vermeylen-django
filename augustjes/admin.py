from django.contrib import admin
from .models import Augustje, Subscriber

class AugustjeAdmin(admin.ModelAdmin):
    list_display = ('edition','date')

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'room')
    
admin.site.register(Augustje, AugustjeAdmin)
admin.site.register(Subscriber, SubscriberAdmin)