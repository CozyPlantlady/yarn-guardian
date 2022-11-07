from django.forms import ModelForm
from django import forms
from .models import Yarn, Project


class AddYarnForm(ModelForm):

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

    WEIGHT_CHOICES = (
        ('LACE', 'Lace'),
        ('SUPERFINE', 'Super Fine'),
        ('FINE', 'Fine'),
        ('LIGHT', 'Light'),
        ('MEDIUM', 'Medium'),
        ('BULKY', 'Bulky'),
        ('SUPERBULKY', 'Super Bulky'),
    )

    MATERIAL_CHOICES = (
        ('WO', 'Wool'),
        ('WP', 'Alpaca'),
        ('WS', 'Cashmere'),
        ('WM', 'Mohair'),
        ('WA', 'Angora'),
        ('WL', 'Llama'),
        ('CO', 'Cotton'),
        ('SE', 'Silk'),
        ('LI', 'Linen'),
        ('PC', 'Acrylic'),
        ('PL', 'Polyester'),
        ('RA', 'Ramie'),
        ('AF', 'Other Fibers'),
    )

    color_group = forms.ChoiceField(choices=COLOR_CHOICES)
    weight = forms.ChoiceField(choices=WEIGHT_CHOICES)
    material = forms.ChoiceField(choices=MATERIAL_CHOICES)

    class Meta:
        model = Yarn
        fields = ['producer', 'name', 'body', 'color_group', 'color_name',
                  'color_code', 'amount', 'weight', 'material', 'favorite', ]


class AddProjectForm(ModelForm):
    name = forms.TextInput()
    body = forms.Textarea()
    yarn = forms.TextInput()

    class Meta:
        model = Project
        fields = ['name', 'body', 'yarn', ]
