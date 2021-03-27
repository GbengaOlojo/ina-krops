from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)
