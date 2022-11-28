from django.urls import path
from . import views

app_name = 'Namyangju'

urlpatterns = [
    path('', views.index, name='index')
]