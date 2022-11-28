from django.urls import path
from . import views

app_name = 'Anyang'

urlpatterns = [
    path('', views.index, name='index')
]