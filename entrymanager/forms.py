from django import forms

from .models import Division

class ContestantEntryForm(forms.Form):    
    legal_name = forms.CharField(label="Legal name", max_length=100)
    email_address = forms.CharField(label="E-mail address", max_length=100)
    cosplay_name = forms.CharField(label="Cosplay Handle/Name to be Called", max_length=100)
    preferred_pronouns = forms.CharField(label="Preferred Pronouns", max_length=15)
    character = forms.CharField(label="Character(s)", max_length=100)
    series = forms.CharField(label="Series", max_length=100)
    division = forms.ChoiceField(label="Division",choices=Division.VALID_DIVISIONS)

class NumBadgeStickersForm(forms.Form):
    numprint = forms.IntegerField(label="Number of stickers to print",min_value=0,max_value=9)
    
