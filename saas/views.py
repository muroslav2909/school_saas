from django.shortcuts import render


def home(request):
    context = {}
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


