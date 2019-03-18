from django.contrib import admin
from .models import Input

class InputAdmin(admin.ModelAdmin):
    list_display = ('input','created_at',)
    
admin.site.register(Input, InputAdmin)