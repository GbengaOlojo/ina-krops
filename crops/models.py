from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=100, null=False)
    company = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    phone = models.CharField(max_length=20, null=False)
    title = models.CharField(max_length=100, null=False, default='SOME STRING')
    slug = models.SlugField()
    message = models.TextField(max_length=1000, null=False)


    def __str__(self):
        return self.full_name


