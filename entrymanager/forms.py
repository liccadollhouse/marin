from django import forms

from .models import Division

class ContestantEntryForm(forms.Form):
    legal_name = forms.CharField(label="Legal name", max_length=100)
    cosplay_name = forms.CharField(label="Cosplay Handle/Name to be Called", max_length=100)
    character = forms.CharField(label="Character(s)", max_length=100)
    series = forms.CharField(label="Series", max_length=100)
    division = forms.ChoiceField(label="Division",choices=Division.VALID_DIVISIONS)
