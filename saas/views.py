from django.shortcuts import render


def home(request):
    context = {}
    return render(request, "auth/login.html", context)

def register(request):
    context = {}
    return render(request, "auth/register.html", context)