# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-06 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comfort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
