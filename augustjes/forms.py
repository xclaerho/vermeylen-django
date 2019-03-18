from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(SubscriberForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['consent'].required = True
    class Meta:
        model = Subscriber
        fields = ['name', 'room', 'email', 'consent']