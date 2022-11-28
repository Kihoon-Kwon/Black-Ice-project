from django.urls import path
from . import views

app_name = 'Goyang'

urlpatterns = [
    path('', views.index, name='index')
]