from django.urls import path
from . import views

app_name = 'Gwacheon'

urlpatterns = [
    path('', views.index, name='index')
]