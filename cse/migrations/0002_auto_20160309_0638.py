# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='mailid',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]