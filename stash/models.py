from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Producer(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Yarn(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
#    user = models.ForeignKey(User)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE,)
#    yarn_type = models.ForeignKey(Yarntype)
#    color = 
#    amount =
    exists = models.BooleanField(default=True)

    def __str__(self):
        return self.name
