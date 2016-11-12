from django.contrib import admin
from saas.models import *


class PTABoardAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PTABoard._meta.fields]
admin.site.register(PTABoard, PTABoardAdmin)

class SchoolAdmin(admin.ModelAdmin):
    list_display = [f.name for f in School._meta.fields]
admin.site.register(School, SchoolAdmin)

class VolunteerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Volunteer._meta.fields]
admin.site.register(Volunteer, VolunteerAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Task._meta.fields]
admin.site.register(Task, TaskAdmin)

class ExpensesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Expenses._meta.fields]
admin.site.register(Expenses, ExpensesAdmin)

class AdminAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Admin._meta.fields]
admin.site.register(Admin, AdminAdmin)

class JudgeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Judge._meta.fields]
admin.site.register(Judge, JudgeAdmin)

class ParentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Parent._meta.fields]
admin.site.register(Parent, ParentAdmin)

class ChildAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Child._meta.fields]
admin.site.register(Child, ChildAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Entry._meta.fields]
admin.site.register(Entry, EntryAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Result._meta.fields]
admin.site.register(Result, ResultAdmin)

class Image_LogoAdmin(admin.ModelAdmin):
    list_display = ['path', 'created', 'updated']
admin.site.register(Image_Logo, Image_LogoAdmin)

