from django.urls import path
from . import views


app_name = 'my_app_name2'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('hello/', views.hello, name='hello')
]