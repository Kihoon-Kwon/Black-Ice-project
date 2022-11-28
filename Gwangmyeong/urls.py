from django.urls import path
from . import views

app_name = 'Gwangmyeong'

urlpatterns = [
    path('', views.index, name='index')
]