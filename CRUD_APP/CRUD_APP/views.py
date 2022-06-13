from django.shortcuts import render
from django.template import loader

# Just for testing hehe
def index(request):
    template = loader.get_template('main.html')
    return render(request, template_name='main.html')