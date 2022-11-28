from django.urls import path
from . import views

app_name = 'Gimpo'

urlpatterns = [
    path('', views.index, name='index')
]