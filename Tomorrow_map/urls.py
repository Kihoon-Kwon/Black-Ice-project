from django.urls import path
from . import views

app_name = 'Tomorrow_map'

urlpatterns = [
    path('', views.index, name='index')
]