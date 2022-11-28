from django.urls import path
from . import views

app_name = 'Hanam'

urlpatterns = [
    path('', views.index, name='index')
]