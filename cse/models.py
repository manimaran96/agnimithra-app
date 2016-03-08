from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    mailid = models.CharField(max_length=30, primary_key=True)
    candidate = models.CharField(max_length=150)
    college = models.CharField(max_length=150)
