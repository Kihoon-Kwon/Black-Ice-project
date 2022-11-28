from django.urls import path
from . import views

app_name = 'Gapyeong'

urlpatterns = [
    path('', views.index, name='index')
]