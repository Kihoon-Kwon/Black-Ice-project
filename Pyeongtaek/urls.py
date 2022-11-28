from django.urls import path
from . import views

app_name = 'Pyeongtaek'

urlpatterns = [
    path('', views.index, name='index')
]