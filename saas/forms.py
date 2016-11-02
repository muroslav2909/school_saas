
from django import forms

class FirstStepRegistration(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=100)

class ParentRegistration(forms.Form):
    school = forms.CharField()
    address1 = forms.CharField()
    address2 = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.IntegerField()
    phone = forms.CharField()


class JudgesRegistration(forms.Form):
    organisation = forms.CharField()
    category = forms.CharField()
    phone = forms.CharField()


class ChairRegistration(forms.Form):
    school = forms.CharField()
    address_1 = forms.CharField()
    address_2 = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.IntegerField()
    phone = forms.CharField()