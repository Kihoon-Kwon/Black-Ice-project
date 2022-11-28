from django.shortcuts import render


def index(request):
    return render(request, 'Gwacheon_main.html')