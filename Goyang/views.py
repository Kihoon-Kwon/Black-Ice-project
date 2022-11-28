from django.shortcuts import render


def index(request):
    return render(request, 'Goyang_main.html')