from django import forms
from .models import Lightning


class LightningForm(forms.ModelForm):

    class Meta:
        model = Lightning
        fields = ('location', 'message',)
