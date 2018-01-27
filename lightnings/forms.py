from django import forms
from .models import Lightning, Catch


class LightningForm(forms.ModelForm):

    class Meta:
        model = Lightning
        fields = ('location', 'message',)


