from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from saas.forms import FirstStepRegistration, ParentRegistration, JudgesRegistration, ChairRegistration
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from saas.models import Parent, School, Judge, Admin
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)

def home(request):
    context = {}
    auth_logout(request)
    if request.method == 'POST' and request.POST['post']:
        email = request.POST['email']
        password = request.POST['password']
        auth = authenticate(username=email, password=password)
        # if auth is not None:
        #     login(request, auth)
            # auth_login(request, User.objects.get(username=email, password=password))
        return redirect("/main")
        # else:
        #     context = {'er1': 'yes'}
    return render(request, "auth/login.html", context)

def register(request):
    context = {}
    auth_logout(request)
    if request.method == 'POST' and request.POST['post']:
        form = FirstStepRegistration(request.POST)
        if form.is_valid():
            role = request.POST['role']
            full_name = form.cleaned_data['full_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            auth = authenticate(username=email, password=password)
            if auth is not None:
                print "auth is not None"
                # login(request, auth)
                # auth_login(request, User.objects.get(username=email, password=password))
                return redirect("/main")
            user = User(username=email, email=email, password=password)
            user.save()
            # auth = authenticate(username=email, password=password)
            # login(request, auth)
            path = "%s_register" % role
            return redirect(path)
    return render(request, "auth/register.html", context)

# @login_required#(login_url='/')
def parent_register(request):
    schools = School.objects.all()
    context = {"schools": schools}
    if request.method == 'POST' and request.POST['post']:
        form = ParentRegistration(request.POST)
        if form.is_valid():
            school = School.objects.get(name=form.cleaned_data['school'])
            mailing_address_1 = form.cleaned_data['address1']
            mailing_address_2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            phone = form.cleaned_data['phone']
            #request.user
            parent, created = Parent.objects.get_or_create(user=User.objects.filter()[0], defaults = {'mailing_address_1': mailing_address_1, 'mailing_address_2': mailing_address_2, 'state': state, 'city': city, 'zipcode': zipcode, 'phone': phone})
            parent.school.add(school)
            parent.save()
            return redirect('/main')
        else:
            context = {'er1': 'yes', "schools": schools}
    return render(request, "auth/parent_register.html", context)

# @login_required#(login_url='/')
def judges_register(request):
    context = {}
    if request.method == 'POST' and request.POST['post']:
        form = JudgesRegistration(request.POST)
        if form.is_valid():
            organisation = form.cleaned_data['organisation']
            phone = form.cleaned_data['phone']
            category = form.cleaned_data['category']
            judge, created = Judge.objects.get_or_create(user=User.objects.filter()[0],
                                                           defaults={'organisation': organisation,
                                                                     'phone': phone})
            judge.save()
            return redirect('/main')
    return render(request, "auth/judges_register.html", context)

def chair_register(request):
    context = {}
    if request.method == 'POST' and request.POST['post']:
        form = ChairRegistration(request.POST)
        if form.is_valid():
            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            phone = form.cleaned_data['phone']
            school = School(name=form.cleaned_data['school'], address_1=address_1, address_2=address_2, city=city, state=state, zipcode=zipcode)
            school.save()
            admin, created = Admin.objects.get_or_create(user=User.objects.filter()[0], defaults={'phone': phone})
            admin.school.add(school)
            admin.save()

            return redirect('/main')
    return render(request, "auth/chair_register.html", context)

# @login_required
def main(request):
    context = {}
    # print "request.userrequest.userrequest.userrequest.userrequest.userrequest.user", request.user
    # try:
    #     p = Parent.objects.get(user=request.user)
    # except: p = None
    # try:
    #     j = Judge.objects.get(user=request.user)
    # except:
    #     j = None
    # try:
    #     c = Admin.objects.get(user=request.user)
    # except:
    #     c = None
    # if p:
    #     return render(request, "auth/parent.html", context)
    # if j:
    #     return render(request, "auth/judges.html", context)
    # if c:
    return render(request, "auth/parent.html", context)

