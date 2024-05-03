# skills/models.py
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=20)
    # Add other fields as necessary
