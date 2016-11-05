from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from saas.forms import FirstStepRegistration, ParentRegistration, JudgesRegistration, ChairRegistration
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from saas.models import Parent, School, Judge, Admin

def home(request):
    context = {}
    # if request.method == 'POST' and request.POST['post']:
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user, created = User.objects.get_or_create(username=email, password=password)
    #     if not created:
    #         print "not created"
    #         logout(request)
    #         user.backend = 'django.contrib.auth.backends.ModelBackend'
    #         user.save()
    #         auth = authenticate(username=email, password=password)
    #         login(request, user)
    #         return redirect("/main")
    #     else:
    #         context = {'er1': 'yes'}
    return render(request, "landing.html", context)


def main_login(request):
    context = {}
    if request.method == 'POST' and request.POST['post']:
        email = request.POST['email']
        password = request.POST['password']
        user, created = User.objects.get_or_create(username=email, password=password)
        if not created:
            print "not created"
            logout(request)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            auth = authenticate(username=email, password=password)
            login(request, user)
            return redirect("/main")
        else:
            context = {'er1': 'yes'}
    return render(request, "auth/login.html", context)

def register(request):
    context = {}
    if request.method == 'POST' and request.POST['post']:
        form = FirstStepRegistration(request.POST)
        if form.is_valid():
            # role = request.POST['role']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user, created = User.objects.get_or_create(username=email, password=password)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            auth = authenticate(username=user.username, password=user.password)
            if not created:
                login(request, auth)
                return redirect("/main")

            login(request, user)
            # path = "%s_register" % role

            return redirect("/intermid")
    return render(request, "auth/register.html", context)

def forgot_password(request):
    context = {}
    return render(request, "auth/forgot_password.html", context)

@login_required
def intermid(request):
    context = {}
    # if request.method == 'POST' and request.POST['post']:
    #     form = FirstStepRegistration(request.POST)
    #     if form.is_valid():
    #         role = request.POST['role']
    #         password = form.cleaned_data['password']
    #         email = form.cleaned_data['email']
    #         user, created = User.objects.get_or_create(username=email, password=password)
    #         user.backend = 'django.contrib.auth.backends.ModelBackend'
    #         user.save()
    #         auth = authenticate(username=user.username, password=user.password)
    #         if not created:
    #             login(request, auth)
    #             return redirect("/main")
    #
    #         login(request, user)
    #         path = "%s_register" % role
    #
    #         return redirect(path)
    return render(request, "itermid_registr_page.html", context)


@login_required
def parent_register(request):
    print "request.userrequest.userrequest.userrequest.userrequest.userrequest.user", request.user
    schools = School.objects.all()
    context = {"schools": schools}
    if request.method == 'POST' and request.POST['post']:
        form = ParentRegistration(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            school = School.objects.get(name=form.cleaned_data['school'])
            mailing_address_1 = form.cleaned_data['address1']
            mailing_address_2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            phone = form.cleaned_data['phone']
            parent, created = Parent.objects.get_or_create(user=request.user, defaults = {'first_name': first_name, 'last_name': last_name, 'mailing_address_1': mailing_address_1, 'mailing_address_2': mailing_address_2, 'state': state, 'city': city, 'zipcode': zipcode, 'phone': phone})
            parent.school.add(school)
            parent.save()
            return redirect('/main')
    return render(request, "auth/parent_register.html", context)

@login_required
def judges_register(request):
    context = {}
    if request.method == 'POST' and request.POST['post']:
        form = JudgesRegistration(request.POST)
        if form.is_valid():
            organisation = form.cleaned_data['organisation']
            phone = form.cleaned_data['phone']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            judge, created = Judge.objects.get_or_create(user=request.user,
                                                           defaults={'organisation': organisation,
                                                                     'first_name': first_name,
                                                                     'last_name': last_name,
                                                                     'phone': phone,
                                                                     })
            judge.save()
            return redirect('/main')
    return render(request, "auth/judges_register.html", context)

@login_required
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
            pta_paid_date = form.cleaned_data['pta_paid_date']
            pta_paid = form.cleaned_data['pta_paid']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            school = School(name=form.cleaned_data['school'], pta_paid=pta_paid, pta_paid_date=pta_paid_date, address_1=address_1, address_2=address_2, city=city, state=state, zipcode=zipcode)
            school.save()
            admin, created = Admin.objects.get_or_create(user=request.user, defaults={'phone': phone,
                                                                                      'first_name': first_name,
                                                                                      'last_name': last_name,
                                                                                      })
            admin.school.add(school)
            admin.save()

            return redirect('/main')
    return render(request, "auth/chair_register.html", context)

@login_required
def main(request):
    context = {}
    print "request.userrequest.userrequest.userrequest.userrequest.userrequest.user", request.user
    try:
        if Parent.objects.get(user=request.user):
            return render(request, "auth/parent.html", context)
    except:
        pass
    try:
        if Judge.objects.get(user=request.user):
            return render(request, "auth/judges.html", context)
    except:
        pass
    try:
        if Admin.objects.get(user=request.user):
            return render(request, "auth/chair.html", context)
    except:
        pass

