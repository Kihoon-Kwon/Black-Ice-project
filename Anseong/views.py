from django.shortcuts import render


def index(request):
    return render(request, 'Anseong_main.html')