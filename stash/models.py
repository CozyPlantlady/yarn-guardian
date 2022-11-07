from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Yarn(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default='')
    producer = models.CharField(max_length=50, null=False, blank=False)
    color = models.CharField(max_length=10, null=True, blank=True, default='')
    amount = models.IntegerField(null=True, blank=True, default='')
    weight = models.CharField(max_length=10, null=True, blank=True, default='')
    material = models.CharField(max_length=15, null=True, blank=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default='')
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE, default='')
    frogged = models.BooleanField(default=False)

    def __str__(self):
        return self.name
