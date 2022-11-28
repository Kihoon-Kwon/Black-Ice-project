from django.shortcuts import render


def index(request):
    return render(request, 'Dongducheon_main.html')