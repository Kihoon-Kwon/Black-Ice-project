from django.shortcuts import render


def index(request):
    return render(request, 'Gapyeong_main.html')