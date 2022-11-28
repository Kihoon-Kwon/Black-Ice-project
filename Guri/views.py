from django.shortcuts import render


def index(request):
    return render(request, 'Guri_main.html')