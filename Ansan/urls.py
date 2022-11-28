from django.urls import path
from . import views

app_name = 'Ansan'

urlpatterns = [
    path('', views.index, name='index')
]