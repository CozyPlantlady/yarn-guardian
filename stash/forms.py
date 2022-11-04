from django.forms import ModelForm
from django import forms
from .models import Yarn


class AddYarnForm(ModelForm):
    name = forms.TextInput()
    body = forms.Textarea()
    producer = forms.TextInput()
    color = forms.TextInput()
    amount = forms.NumberInput()
    weight = forms.TextInput()
    material = forms.TextInput()
    favorite = forms.BooleanField()

    class Meta:
        model = Yarn
        fields = ['name', 'body', 'producer', 'color', 'amount',
                  'weight', 'material', 'favorite', ]
