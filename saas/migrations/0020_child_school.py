# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0019_taskfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='school',
            field=models.ManyToManyField(to='saas.School'),
        ),
    ]