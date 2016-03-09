from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key=True, default=1) 
    mailid = models.CharField(max_length=30, unique=True)
    candidate = models.CharField(max_length=50)
    college = models.CharField(max_length=150)
