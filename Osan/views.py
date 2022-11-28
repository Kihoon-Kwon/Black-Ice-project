from django.shortcuts import render


def index(request):
    return render(request, 'Osan_main.html')