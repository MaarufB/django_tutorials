from django.urls import path
from employee.views import (test, get_employees)
app_name = 'employee'

urlpatterns = [
    path('test/', test, name='test'),
    path('get_employees/', get_employees, name='get_employees'),
]