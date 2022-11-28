from django.urls import path
from . import views

app_name = 'Gunpo'

urlpatterns = [
    path('', views.index, name='index')
]