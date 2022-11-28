from django.shortcuts import render


def index(request):
    return render(request, 'Gwangmyeong_main.html')