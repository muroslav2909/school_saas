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
    return render(request, "auth/login.html", context)

def register(request):
    context = {}
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


