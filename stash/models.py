from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Producer(models.Model):
    producer = models.CharField(max_length=30)
    body = models.TextField()

    def __str__(self):
        return self.producer
