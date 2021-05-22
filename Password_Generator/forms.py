from .models import Registration
from django import forms
from pytz import country_names as c

dict_choices = dict(c)
_choices = []
_keys = list(dict_choices.keys())
_value = list(dict_choices.values())

if len(_keys) == len(_value):
    for i in range(len(_keys)):
        a = [_keys[i], _value[i]]
        _choices.append(tuple(a))


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

'''
    Name = forms.CharField(max_length=300)
    Email = forms.EmailField(max_length=300)
    Contact_Number = forms.IntegerField()
    Organization = forms.CharField(max_length=300)
    Country = forms.ChoiceField(choices=_choices)
'''