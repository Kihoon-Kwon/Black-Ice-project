from django.urls import path
from . import views

app_name = 'Guri'

urlpatterns = [
    path('', views.index, name='index')
]