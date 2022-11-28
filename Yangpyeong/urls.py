from django.urls import path
from . import views

app_name = 'Yangpyeong'

urlpatterns = [
    path('', views.index, name='index')
]