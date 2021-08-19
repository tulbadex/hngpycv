from django.db import models

# Create your models here.
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contacts:contact')
