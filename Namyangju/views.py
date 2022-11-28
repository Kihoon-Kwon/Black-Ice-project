from django.shortcuts import render


def index(request):
    return render(request, 'Namyangju_main.html')