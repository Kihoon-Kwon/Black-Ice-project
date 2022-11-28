from django.urls import path
from . import views

app_name = 'Pocheon'

urlpatterns = [
    path('', views.index, name='index')
]