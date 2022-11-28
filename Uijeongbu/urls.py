from django.urls import path
from . import views

app_name = 'Uijeongbu'

urlpatterns = [
    path('', views.index, name='index')
]