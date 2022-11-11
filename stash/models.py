from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Yarn(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False)
    body = models.TextField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default='')
    producer = models.CharField(max_length=50)

    color_group = models.CharField(
        max_length=10, blank=True, default='')
    color_name = models.CharField(
        max_length=50, blank=True, default='')
    color_code = models.CharField(
        max_length=6, blank=True, default='')

    amount = models.IntegerField(null=True, blank=True, default='')
    weight = models.CharField(max_length=10, blank=True, default='')
    material = models.CharField(max_length=100, null=True, blank=True)
    favorite = models.BooleanField(blank=True, default=False)
    frogged = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False)
    body = models.TextField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default='')
    link = models.URLField(default='', blank=True)
    yarn = models.ForeignKey(
        Yarn, on_delete=models.SET_NULL, default='', null=True, blank=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name
