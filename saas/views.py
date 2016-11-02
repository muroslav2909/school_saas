from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from saas.forms import FirstStepRegistration, ParentRegistration
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from saas.models import Parent, School


def home(request):
    context = {}
    if request.method == 'POST' and request.POST['post']:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            return render(request, "auth/main.html", context)
        else:
            context = {'er1': 'yes'}

    return render(request, "auth/login.html", context)

def register(request):
    context = {}
    if request.method == 'POST' and request.POST['post']:
        form = FirstStepRegistration(request.POST)
        if form.is_valid():
            role = request.POST['role']
            full_name = form.cleaned_data['full_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            auth = authenticate(username=email, password=password)
            if auth is not None:
                login(request, auth)
                return redirect("/main")
            user = User(username=full_name, email=email, password=password)
            user.save()
            path = "%s_register" % role
            return redirect(path)
    return render(request, "auth/register.html", context)

@login_required
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
            parent, created = Parent.objects.get_or_create(user=request.user, defaults = {'mailing_address_1': mailing_address_1, 'mailing_address_2': mailing_address_2, 'state': state, 'city': city, 'zipcode': zipcode, 'phone': phone})
            parent.school.add(school)
            parent.save()
            return redirect('/main')
        else:
            context = {'er1': 'yes', "schools": schools}
    return render(request, "auth/parent_register.html", context)

def judges_register(request):
    context = {}
    return render(request, "auth/judges_register.html", context)

def chair_register(request):
    context = {}
    return render(request, "auth/chair_register.html", context)

@login_required
def main(request):
    context = {}
    return render(request, "auth/main.html", context)


