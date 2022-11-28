from django.shortcuts import render


def index(request):
    return render(request, 'Gimpo_main.html')