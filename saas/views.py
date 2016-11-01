from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def home(request):
    context = {}
    if request.method == 'POST' and request.POST['email'] and request.POST['password']:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            return render(request, "auth/main.html", context)
        else:
            pass

    return render(request, "auth/login.html", context)

def register(request):
    context = {}
    if request.method == 'POST' and request.POST['email'] and request.POST['full_name'] and request.POST['password'] and request.POST['role']:
        email = request.POST['email']
        password = request.POST['password']
        full_name = request.POST['full_name']
        role = request.POST['role']
        user = User(username=full_name, email=email, password=password)
        user.save()
        path = "auth/%s_register.html" % role
        return render(request, path, context)
    return render(request, "auth/register.html", context)


def parent_register(request):
    context = {}
    return render(request, "auth/parent_register.html", context)

def judges_register(request):
    context = {}
    return render(request, "auth/judges_register.html", context)

def chair_register(request):
    context = {}
    return render(request, "auth/chair_register.html", context)

def main(request):
    context = {}
    return render(request, "auth/main.html", context)


