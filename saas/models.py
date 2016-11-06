from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    address_1 = models.CharField(max_length=100, null=True, blank=True)
    address_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.PositiveIntegerField(max_length=100, null=True, blank=True)
    pta_paid = models.BooleanField(default=False)
    pta_paid_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)

class PTABoard(models.Model):
    role = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    school = models.ManyToManyField(School)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.id)

class Volunteer(models.Model):
    school = models.ManyToManyField(School)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.id)


class Task(models.Model):
    school = models.ManyToManyField(School)
    task_category = models.CharField(max_length=50, null=True, blank=True)
    task_description = models.TextField(max_length=5000, null=True, blank=True)
    task_exp_start_date = models.DateTimeField(null=True, blank=True)
    task_exp_end_date = models.DateTimeField(null=True, blank=True)
    task_actual_start_date = models.DateTimeField(null=True, blank=True)
    task_actual_end_date = models.DateTimeField(null=True, blank=True)
    asignee = models.ManyToManyField(User)

class Expenses(models.Model):
    school = models.ManyToManyField(School)
    expense_category = models.CharField(max_length=50, null=True, blank=True)
    expense_description = models.TextField(max_length=5000, null=True, blank=True)
    expense_date = models.DateTimeField(null=True, blank=True)
    expense_amount = models.IntegerField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    scanned_doc = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    comments = models.CharField(max_length=500, null=True, blank=True)

class Admin(models.Model):
    user = models.ForeignKey(User)
    school = models.ManyToManyField(School)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.id)

class Judge(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    organisation = models.CharField(max_length=50, null=True, blank=True)
    # school = models.ManyToManyField(School)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.id)


class Parent(models.Model):
    user = models.ForeignKey(User)
    school = models.ManyToManyField(School)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    mailing_address_1 = models.CharField(max_length=100, null=True, blank=True)
    mailing_address_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.PositiveIntegerField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.id)


class Child(models.Model):
    parent = models.ManyToManyField(Parent)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    grade = models.CharField(max_length=50, null=True, blank=True)
    class_teacher_name = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.id)

class Entry(models.Model):
    child = models.ManyToManyField(Child)
    grase_division = models.CharField(max_length=50, null=True, blank=True)
    art_category = models.CharField(max_length=50, null=True, blank=True)
    special_art_division = models.CharField(max_length=50, null=True, blank=True)
    title_art_work = models.CharField(max_length=50, null=True, blank=True)
    art_work_details = models.TextField(max_length=5000, null=True, blank=True)
    artist_statements = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.title_art_work)


class Result(models.Model):
    entry = models.ManyToManyField(Entry)
    score_basis_1 = models.PositiveIntegerField(max_length=20, null=True, blank=True)
    score_basis_2 = models.PositiveIntegerField(max_length=20, null=True, blank=True)
    score_basis_3 = models.PositiveIntegerField(max_length=20, null=True, blank=True)
    score_basis_4 = models.PositiveIntegerField(max_length=20, null=True, blank=True)
    total_score = models.PositiveIntegerField(max_length=20, null=True, blank=True)