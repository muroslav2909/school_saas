# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 20:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0023_auto_20161115_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='school',
        ),
    ]
