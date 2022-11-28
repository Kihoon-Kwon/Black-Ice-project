from django.urls import path
from . import views

app_name = 'Gwangju'

urlpatterns = [
    path('', views.index, name='index')
]