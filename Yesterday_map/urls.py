from django.urls import path
from . import views

app_name = 'Yesterday_map'

urlpatterns = [
    path('', views.index, name='index')
]