from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Producer(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    class MaterialType(models.TextChoices):
        WOOL = 'WO', 'Wool'
        ALPACA = 'WP', 'Alpaca'
        CASHMERE = 'WS', 'Cashmere'

    material_type = models.CharField(
        max_length=2,
        choices=MaterialType.choices,
        default=MaterialType.WOOL
    )

    def __str__(self):
        return self.name


class Yarn(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
#    user = models.ForeignKey(User)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE,)
#    yarn_type = models.ForeignKey(Yarntype)
#    color = 
#    amount =
    material = models.ForeignKey(Material, on_delete=models.CASCADE, default='')
    exists = models.BooleanField(default=True)

    def __str__(self):
        return self.name
