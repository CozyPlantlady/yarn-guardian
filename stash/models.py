from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Producer(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Material(models.Model):

    class MaterialType(models.TextChoices):
        WOOL = 'Wool'
        ALPACA = 'Alpaca'
        CASHMERE = 'Cashmere'

    material_type = models.CharField(
        max_length=10,
        choices=MaterialType.choices,
        default=MaterialType.WOOL
    )

    def __str__(self):
        return self.material_type


class Weight(models.Model):

    class WeightType(models.TextChoices):
        LACE = ('0', 'Lace')
        SUPERFINE = ('1', 'Super Fine')
        FINE = ('2', 'Fine')
        LIGHT = ('3', 'Light')
        MEDIUM = ('4', 'Medium')
        BULKY = ('5', 'Bulky')
        SUPERBULKY = ('6', 'Super Bulky')

    weight_type = models.CharField(
        max_length=1,
        choices=WeightType.choices,
        default=WeightType.LIGHT
    )

    def __str__(self):
        return self.weight_type


class Color(models.Model):
    WHITE = 'Wh'
    YELLOW = 'Ye'
    BLUE = 'Bl'
    RED = 'Re'
    GREEN = 'Gr'
    BLACK = 'Bl'
    BROWN = 'Br'
    COLOR_CHOICES = [
        (WHITE, 'White'),
        (YELLOW, 'Yellow'),
        (BLUE, 'Blue'),
        (RED, 'Red'),
        (GREEN, 'Green'),
        (BLACK, 'Black'),
        (BROWN, 'Brown'),
    ]

    color_choice = models.CharField(
        max_length=10,
        choices=COLOR_CHOICES,
        default=WHITE,
    )

    def __str__(self):
        return self.color_choice


class Amount(models.Model):
    amount = models.IntegerField(null=True)

    def __int__(self):
        return self.amount


class Yarn(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default='')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE,)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default='')
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE, default='')
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE, default='')
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, default='')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
