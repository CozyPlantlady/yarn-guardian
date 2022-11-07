from django.forms import ModelForm
from django import forms
from .models import Yarn, Project


COLOR_CHOICES = [
    ('WHITE', 'White'),
    ('YELLOW', 'Yellow'),
    ('BLUE', 'Blue'),
    ('RED', 'Red'),
    ('GREEN', 'Green'),
    ('BLACK', 'Black'),
    ('BROWN', 'Brown'),
    ('PURPLE', 'Purple'),
    ('GRAY', 'Gray'),
]


class AddYarnForm(ModelForm):
    producer = forms.TextInput()
    name = forms.CharField()
    body = forms.TextInput()
    color = forms.ChoiceField(choices=COLOR_CHOICES)
    amount = forms.NumberInput()
    weight = forms.ChoiceField()
    material = forms.ChoiceField()
    favorite = forms.BooleanField()

    class Meta:
        model = Yarn
        fields = ['producer', 'name', 'body', 'color', 'amount',
                  'weight', 'material', 'favorite', ]


class AddProjectForm(ModelForm):
    name = forms.TextInput()
    body = forms.Textarea()
    yarn = forms.TextInput()

    class Meta:
        model = Project
        fields = ['name', 'body', 'yarn', ]
