# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suveen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]