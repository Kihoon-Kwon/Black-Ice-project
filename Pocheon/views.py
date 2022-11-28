from django.shortcuts import render


def index(request):
    return render(request, 'Pocheon_main.html')