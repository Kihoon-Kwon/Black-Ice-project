from django.shortcuts import render


def index(request):
    return render(request, 'Yongin_main.html')