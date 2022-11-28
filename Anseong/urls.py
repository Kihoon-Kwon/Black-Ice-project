from django.urls import path
from . import views

app_name = 'Anseong'

urlpatterns = [
    path('', views.index, name='index')
]