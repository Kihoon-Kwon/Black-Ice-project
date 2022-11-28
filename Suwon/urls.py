from django.urls import path
from . import views

app_name = 'Suwon'

urlpatterns = [
    path('', views.index, name='index')
]