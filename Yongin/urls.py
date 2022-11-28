from django.urls import path
from . import views

app_name = 'Yongin'

urlpatterns = [
    path('', views.index, name='index')
]