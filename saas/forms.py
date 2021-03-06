
from django import forms

class FirstStepRegistration(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)

class ParentRegistration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    school = forms.CharField()
    address1 = forms.CharField()
    address2 = forms.CharField(required = False)
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.IntegerField()
    phone = forms.CharField()


class JudgesRegistration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    organisation = forms.CharField()
    phone = forms.CharField()


class ChairRegistration(forms.Form):
    school = forms.CharField()
    address_1 = forms.CharField()
    address_2 = forms.CharField(required = False)
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    pta_paid = forms.BooleanField(required=False)
    pta_paid_date = forms.DateField(required=False)

class VolunteerRegistration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()

class PTABoardRegistration(forms.Form):
    first_name = forms.CharField()
    role = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()


class SchoolRegistration(forms.Form):
    school = forms.CharField()
    address_1 = forms.CharField()
    address_2 = forms.CharField(required=False)
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.IntegerField()
    pta_paid = forms.BooleanField(required=False)
    pta_paid_date = forms.DateField(required=False)


class TaskRegistration(forms.Form):
    task_category = forms.CharField()
    task_description = forms.CharField(required=False)
    task_exp_start_date = forms.CharField(required=False)
    task_exp_end_date = forms.CharField(required=False)
    task_actual_start_date = forms.CharField(required=False)
    task_actual_end_date = forms.CharField(required=False)
    status = forms.CharField(required=False)
    comments = forms.CharField(required=False)
    asignee = forms.CharField(required=False)

class ParentInvite(forms.Form):
    last_day = forms.CharField()
    email = forms.EmailField()


class JudgeInvite(forms.Form):
    ranking_factors = forms.CharField()
    email = forms.EmailField()

class ImgValidation(forms.Form):
    img_url = forms.CharField(required=True)

class ForgotPass(forms.Form):
    email = forms.EmailField()

class ChildRegistration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    grade = forms.CharField(required=False)
    class_teacher_name = forms.CharField(required=False)
    schools = forms.CharField(required=False)

class ExpensesRegistration(forms.Form):
    expense_category = forms.CharField(required=False)
    expense_description = forms.CharField(required=False)
    expense_date = forms.CharField(required=False)
    expense_amount = forms.CharField(required=False)
    status = forms.CharField(required=False)
    comments = forms.CharField(required=False)
    schools = forms.CharField(required=False)

class EntryRegistration(forms.Form):
    child_id = forms.CharField(required=False)
    grase_division = forms.CharField(required=False)
    art_category = forms.CharField(required=False)
    special_art_division = forms.CharField(required=False)
    title_art_work = forms.CharField(required=False)
    art_work_details = forms.CharField(required=False)
    artist_statements = forms.CharField(required=False)

class ResultRegistration(forms.Form):
    score_basis_1 = forms.CharField(required=False)
    score_basis_2 = forms.CharField(required=False)
    score_basis_3 = forms.CharField(required=False)
    score_basis_4 = forms.CharField(required=False)















