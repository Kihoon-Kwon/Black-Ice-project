from django.shortcuts import render


def index(request):
    return render(request, 'Bucheon_main.html')