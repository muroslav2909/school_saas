# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 17:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('grade', models.CharField(blank=True, max_length=50, null=True)),
                ('class_teacher_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grase_division', models.CharField(blank=True, max_length=50, null=True)),
                ('art_category', models.CharField(blank=True, max_length=50, null=True)),
                ('special_art_division', models.CharField(blank=True, max_length=50, null=True)),
                ('title_art_work', models.CharField(blank=True, max_length=50, null=True)),
                ('art_work_details', models.TextField(blank=True, max_length=5000, null=True)),
                ('artist_statements', models.CharField(blank=True, max_length=50, null=True)),
                ('child', models.ManyToManyField(to='saas.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_category', models.CharField(blank=True, max_length=50, null=True)),
                ('expense_description', models.TextField(blank=True, max_length=5000, null=True)),
                ('expense_date', models.DateTimeField(blank=True, null=True)),
                ('expense_amount', models.IntegerField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('scanned_doc', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('organisation', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mailing_address_1', models.CharField(blank=True, max_length=100, null=True)),
                ('mailing_address_2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.PositiveIntegerField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PTABoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_basis_1', models.PositiveIntegerField(blank=True, max_length=20, null=True)),
                ('score_basis_2', models.PositiveIntegerField(blank=True, max_length=20, null=True)),
                ('score_basis_3', models.PositiveIntegerField(blank=True, max_length=20, null=True)),
                ('score_basis_4', models.PositiveIntegerField(blank=True, max_length=20, null=True)),
                ('total_score', models.PositiveIntegerField(blank=True, max_length=20, null=True)),
                ('entry', models.ManyToManyField(to='saas.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('address_1', models.CharField(blank=True, max_length=100, null=True)),
                ('address_2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.PositiveIntegerField(blank=True, max_length=100, null=True)),
                ('pta_paid', models.BooleanField(default=False)),
                ('pta_paid_date', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('pta', models.ManyToManyField(to='saas.PTABoard')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_category', models.CharField(blank=True, max_length=50, null=True)),
                ('task_description', models.TextField(blank=True, max_length=5000, null=True)),
                ('task_exp_start_date', models.DateTimeField(blank=True, null=True)),
                ('task_exp_end_date', models.DateTimeField(blank=True, null=True)),
                ('task_actual_start_date', models.DateTimeField(blank=True, null=True)),
                ('task_actual_end_date', models.DateTimeField(blank=True, null=True)),
                ('asignee', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('school', models.ManyToManyField(to='saas.School')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('school', models.ManyToManyField(to='saas.School')),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='school',
            field=models.ManyToManyField(to='saas.School'),
        ),
        migrations.AddField(
            model_name='parent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='judge',
            name='school',
            field=models.ManyToManyField(to='saas.School'),
        ),
        migrations.AddField(
            model_name='judge',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expenses',
            name='school',
            field=models.ManyToManyField(to='saas.School'),
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ManyToManyField(to='saas.Parent'),
        ),
        migrations.AddField(
            model_name='admin',
            name='school',
            field=models.ManyToManyField(to='saas.School'),
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
