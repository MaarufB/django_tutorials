import imp
from django.shortcuts import render # this is the shortcut to render a view
from django.http import JsonResponse, HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse

from members.serializers import MemberSerializer
from .models import Members


from asgiref.sync import sync_to_async

import os 
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'

# Create your views here.

# def index(request):
#     template = loader.get_template('members/index.html')

#     return HttpResponse(template.render())

async def get_data_member(self):
    return Members.objects.all().values()

@sync_to_async()
def index(request):
    # create a members object
    members = Members.objects.all().values()
    # members = sync_to_async(get_data_member())

    template = loader.get_template('members/index.html')
    context = {
        'members': members,
    }
    return  HttpResponse(template.render(context, request))

def get_members(request):
    data = Members.objects.all()
    serializer = MemberSerializer(data, many=True)
    context = {"context": serializer.data}
    
    return JsonResponse(context)

def add_view(request):
    template = loader.get_template('members/add_member.html')
    return HttpResponse(template.render({}, request))


def add_member(request):
    firstname = request.POST['first']
    lastname = request.POST['last']
    image = request.POST['image']
    # image = request.FILES
    member = Members(firstname=firstname, lastname=lastname, images_file=image)
    # print(member.images_file)
    member.save()

    return HttpResponseRedirect(reverse('members:index'))

def delete_member(request, member_id):
    # template = loader.get_template('')
    member = Members.objects.get(id=member_id)
    member.delete()
    
    return HttpResponseRedirect(reverse('members:index'))

def update_view(request, member_id):
    member = Members.objects.get(id=member_id)
    template = loader.get_template('members/update_view.html')
    context = {
        'members': member
    }
    return HttpResponse(template.render(context, request))


def update_member(request, member_id):
    firstname = request.POST['first']
    lastname = request.POST['last']
    member:Members = Members.objects.get(id=member_id)
    member.firstname = firstname
    member.lastname = lastname
    member.save()

    return HttpResponseRedirect(reverse('members:index'))