# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0018_auto_20161112_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saas.Task')),
            ],
        ),
    ]
