from django.urls import path
from . import views

app_name = 'Uiwang'

urlpatterns = [
    path('', views.index, name='index')
]