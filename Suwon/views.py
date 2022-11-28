from django.shortcuts import render


def index(request):
    return render(request, 'Suwon_main.html')