from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def backend_home(request):
    return render(request, 'backend_home.html', {})
