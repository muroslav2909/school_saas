# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0012_auto_20161109_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_actual_end_date',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_actual_start_date',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_exp_end_date',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_exp_start_date',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
