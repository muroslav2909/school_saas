# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 22:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0028_auto_20161117_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='entry',
        ),
    ]