from django.forms import ModelForm
from django import forms
from .models import Yarn, Project


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


class AddProjectForm(ModelForm):
    name = forms.TextInput()
    body = forms.Textarea()
    yarn = forms.TextInput()

    class Meta:
        model = Project
        fields = ['name', 'body', 'yarn', ]
