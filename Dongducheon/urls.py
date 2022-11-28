from django.urls import path
from . import views

app_name = 'Dongducheon'

urlpatterns = [
    path('', views.index, name='index')
]