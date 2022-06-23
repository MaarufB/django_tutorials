from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    # add logic here
    return render(request, 'index.html', {})

def room(request, room_name):
    # add logic here
    return render(request, 'chatroom.html', {
        'room_name':room_name
    })