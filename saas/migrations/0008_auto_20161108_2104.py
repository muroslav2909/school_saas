# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0007_task_asignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comments',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('new', 'NEW'), ('in_progress', 'IN_PROGRESS'), ('done', 'DONE')], max_length=50, null=True),
        ),
    ]
