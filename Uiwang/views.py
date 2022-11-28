from django.shortcuts import render


def index(request):
    return render(request, 'Uiwang_main.html')