from unicodedata import name
from django.urls import path
from . import views

app_name = 'my_app_name'

urlpatterns = [
    path('test/', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
]