from django.shortcuts import render


def index(request):
    return render(request, 'Yeoju_main.html')