from django.forms import ModelForm
from django import forms
from .models import Yarn, Project


class AddYarnForm(ModelForm):

    COLOR_CHOICES = [
        ('White', 'White'),
        ('Yellow', 'Yellow'),
        ('Blue', 'Blue'),
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('Black', 'Black'),
        ('Brown', 'Brown'),
        ('Purple', 'Purple'),
        ('Gray', 'Gray'),
    ]

    WEIGHT_CHOICES = (
        ('Lace', 'Lace'),
        ('Super Fine', 'Super Fine'),
        ('Fine', 'Fine'),
        ('Light', 'Light'),
        ('Medium', 'Medium'),
        ('Bulky', 'Bulky'),
        ('Super Bulky', 'Super Bulky'),
    )

    MATERIAL_CHOICES = (
        ('Wool', 'Wool'),
        ('Alpaca', 'Alpaca'),
        ('Cashmere', 'Cashmere'),
        ('Mohair', 'Mohair'),
        ('Angora', 'Angora'),
        ('Llama', 'Llama'),
        ('Cotton', 'Cotton'),
        ('Silk', 'Silk'),
        ('Linen', 'Linen'),
        ('Acrylic', 'Acrylic'),
        ('Polyester', 'Polyester'),
        ('Ramie', 'Ramie'),
        ('Other Fibers', 'Other Fibers'),
    )

    color_group = forms.ChoiceField(choices=COLOR_CHOICES)
    weight = forms.ChoiceField(choices=WEIGHT_CHOICES)
    material = forms.MultipleChoiceField(
        choices=MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple())

    def clean_my_field(self):
        if len(self.cleaned_data['material']) > 3:
            raise forms.ValidationError('You can select up to 3.')
        return self.cleaned_data['my_field']

    class Meta:
        model = Yarn
        fields = ['producer', 'name', 'body', 'color_group', 'color_name',
                  'color_code', 'amount', 'weight', 'material', 'favorite',
                  'frogged', ]


class AddProjectForm(ModelForm):
    name = forms.TextInput()
    body = forms.Textarea()
    link = forms.URLField()
    yarn = forms.TextInput()

    class Meta:
        model = Project
        fields = ['name', 'body', 'link', 'yarn', 'finished', ]
