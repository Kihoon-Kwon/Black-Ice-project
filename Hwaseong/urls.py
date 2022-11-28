from django.urls import path
from . import views

app_name = 'Hwseong'

urlpatterns = [
    path('', views.index, name='index')
]