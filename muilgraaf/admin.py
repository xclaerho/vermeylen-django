from django.contrib import admin
from .models import Person, Link
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ['created_by']

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ['created_by']

admin.site.register(Person, PersonAdmin)
admin.site.register(Link, LinkAdmin)