from django.urls import path
from . import views

app_name = 'Siheung'

urlpatterns = [
    path('', views.index, name='index')
]