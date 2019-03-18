from django import forms
from .models import Person, Link

class PersonAddForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'club']

class LinkAddForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['pid','sid','link_type','date','location']