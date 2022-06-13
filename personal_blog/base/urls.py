from os import urandom
from django.urls import path

from . import views

app_name = 'base'
urlpatterns = [
    path('index/', views.index, name='index'),
]