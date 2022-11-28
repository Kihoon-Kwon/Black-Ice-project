from django.shortcuts import render


def index(request):
    return render(request, 'Pyeongtaek_main.html')