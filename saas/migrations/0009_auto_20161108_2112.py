# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0008_auto_20161108_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]