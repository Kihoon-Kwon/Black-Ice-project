from django.urls import path
from . import views

app_name = 'Yeoju'

urlpatterns = [
    path('', views.index, name='index')
]