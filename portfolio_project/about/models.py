# about/models.py
from django.db import models

class About(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # Add other fields as necessary
