from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model): 
    mailid = models.CharField(primary_key=True)
    mailid = models.CharField(max_length=30, unique=True)
    candidate = models.CharField(max_length=50)
    college = models.CharField(max_length=150)
