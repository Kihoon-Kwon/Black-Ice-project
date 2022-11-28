from django.shortcuts import render


def index(request):
    return render(request, 'Siheung_main.html')