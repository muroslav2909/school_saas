# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 21:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0009_auto_20161108_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='asignee',
        ),
    ]
