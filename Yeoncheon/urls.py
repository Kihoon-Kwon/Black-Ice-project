from django.urls import path
from . import views

app_name = 'Yeoncheon'

urlpatterns = [
    path('', views.index, name='index')
]