from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Employees

# Create your views here.
def test(request):
    return render(request, template_name='employee/test.html')
    
def employee_list(request):
    pass

def add_employee(request):
    pass

def update_employee(request):
    pass

def delete_employee(request):
    pass

def get_employees(request):
    data = Employees.objects.all()
    # print(data)
    context = {'employees': data}
    return render(request, template_name='employee/test.html', context=context)


def get_employee(request, id):
    pass
