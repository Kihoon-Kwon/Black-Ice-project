from django.urls import path
from . import views

app_name = 'Incheon'

urlpatterns = [
    path('', views.index, name='index')
]