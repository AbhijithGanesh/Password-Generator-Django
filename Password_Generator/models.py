from django.db import models
from pytz import country_names as c
from datetime import date

dict_choices = dict(c)
_choices = []
_keys = list(dict_choices.keys())
_value = list(dict_choices.values())
if len(_keys) == len(_value):
    for i in range(len(_keys)):
        a = [_keys[i],_value[i]]
        _choices.append(tuple(a))
class Registration(models.Model):
    Name = models.CharField(max_length = 300)
    Email = models.EmailField(max_length = 300)
    Contact_Number = models.IntegerField()
    Organization = models.CharField(max_length = 300)
    Country = models.CharField(max_length = 75, choices = _choices )

