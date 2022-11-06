from django.forms import ModelForm
from django import forms
from .models import Yarn, Project, ColorGroup


class AddYarnForm(ModelForm):
    producer = forms.TextInput()
    name = forms.CharField()
    body = forms.TextInput()
    color = forms.ModelChoiceField(queryset=ColorGroup.objects.all())
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
