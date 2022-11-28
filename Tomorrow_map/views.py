from django.shortcuts import render


def index(request):
    return render(request, 'Tomorrow_main.html')