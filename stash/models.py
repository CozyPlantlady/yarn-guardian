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

    class ColorChoices(models.TextChoices):
        WHITE = 'White'
        YELLOW = 'Yellow'
        BLUE = 'Blue'
        RED = 'Red'
        GREEN = 'Green'
        BLACK = 'Black'
        BROWN = 'Brown'

    color_choice = models.CharField(
        max_length=10,
        choices=ColorChoices.choices,
        default=ColorChoices.WHITE
    )

    def __str__(self):
        return self.color_choice


class Yarn(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
#    user = models.ForeignKey(User)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE,)
#    yarn_type = models.ForeignKey(Yarntype)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default='')
#    amount =
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE, default='')
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, default='')
    exists = models.BooleanField(default=True)

    def __str__(self):
        return self.name
