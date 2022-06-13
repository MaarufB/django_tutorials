from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from form_app.serializers import ProjectSerializer
from .models import (Movie, Project)
from .forms import (ContactForm, MovieForm, NameForm, BookForm, ProjectForm)
from django.contrib import messages
#add email module
from django.core.mail import send_mail
# Create your views here.


def index(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES)
        if movie_form.is_valid():
            movie_form.save()
            messages.success(request, "You Movie was successfully ADDED!")
        else:
            messages.error(request, "Error saving form")

        return redirect("form_app:index")

    movie_form = MovieForm()
    movies = Movie.objects.all()

    return render(
                    request=request, 
                    template_name='form_app/index.html', 
                    context={
                        'movie_form': movie_form, 
                        'movies': movies
                        })



def get_name(request):
    # If this is a POST Request we need to process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        #Check whether it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'form_app/name_list.html', {'form': form})

def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message =form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            
            recipients = ['maarufburad1231@gmail.com']
            if cc_myself:
                recipients.append[sender]

            send_mail(subject, message, sender, recipients)

            return HttpResponse('<h1>Email Sends</h1>')

    else:
        form = ContactForm()

    return render(request, 'form_app/contact_me.html', {'form': form})



def author_list(request):
    if request.method == "POST":
        pass

    else:
        pass



def book_list(request):
    if request.method == "POST":
        pass
    

def book_view(request):
    context = {}

    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] =  form
    return render(request, )

def get_projects(request):
    project_list = Project.objects.all()
    serializer = ProjectSerializer(project_list, many=True)

    context = {"projects": serializer.data}
    print(project_list)
    

    return render(request, 'form_app/project_list.html', context)
    # return JsonResponse(context)

def createProject(request):
    context = {}
    form = ProjectForm()
    if request.method == "POST":
        # print(f"FORM DATA: {request.POST}")
        # title = request.POST["title"]
        # desc = request.POST['description']
        form = ProjectForm(request.POST)
        if form.is_valid():
            
            form.save()
            print(f"Form is saved!")

        return redirect("form_app:get_projects")
        # print(f"title: {title}\ndescription: {desc}")
            
        # create_data = Project.objects.create(
        #     title=title, description=desc
        # )
        

    context['form'] = form
    # print(f"{context['form']}")


    return render(request, 'form_app/create_project.html',context)

def update_project(request, pk):
    context = {}
    project = Project.objects.get(id=pk)

    form = ProjectForm(instance = project)
    if request.method == "POST":
        form =  ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()

            return redirect("form_app:get_projects")

    context["form"] = form

    return render(request, "form_app/create_project.html", context)

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        print(f"Project deleted!")

        return redirect("form_app:get_projects")

    return render(request, 'form_app/delete_project.html', {'object': project})