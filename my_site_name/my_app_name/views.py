from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Index!</h1>')

def hello(request):
    return HttpResponse('<h1>Hello</h1>')