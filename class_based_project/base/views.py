from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from .forms import TaskForm

# Create your views here.

from django.views import View

from django.views.generic import (
                ListView, 
                TemplateView, 
                DeleteView,
                DetailView,
                CreateView
                )

class IndexView(TemplateView):
    template_name: str = "base/home.html"


class TaskList(ListView):
    model = Task
    context_object_name = "tasks"
    template_name: str = "tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class TaskUpsertView(View):
    def __init__(self):
        self.form_class = TaskForm
        self.initial = {'test': 'test'}
        self.template_name = 'base/upsert.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        print(f'kwargs: {kwargs}')
        print(f'args: {args}')
        if 'id' in kwargs:
            task = Task.objects.get(id=kwargs['id'])
            form = self.form_class(instance=task)
    
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        if not 'id' in kwargs:
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            task = Task.objects.get(id=kwargs['id'])
            form = self.form_class(request.POST, instance=task)
            if form.is_valid():
                form.save()
                print(f"Task is updated!")
                return redirect('index')

        return render(request, self.template_name, {'form': form}) 

# decorators

decorators = [never_cache, login_required]

@method_decorator(decorators, name='dispatch')
class ProtectedView(TemplateView):
    template_name: str = "secret.html"

    # or use the above decorator
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)




# This part here is the generic views
class PublisherListView(ListView):
    # you need to specify the model name here
    model = Publisher

    # override the default object context name
    context_object_name = 'my_favorite_publishers'


class PublisherDetailView(DetailView):
    # model = Publisher
    context_object_name = 'publisher'
    template_name: str = 'base/book_detail.html'

    queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        # Call The base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print(f"This is publisher {kwargs}")
        context['book_list'] = Book.objects.all()
        
        return context
    # This implementation of the get_context_data function
    # we can use queryset argument at class level to query the data from the database

    """
    Specifying model = Publisher is shorthand for saying queryset = Publisher.objects.all(). 
    However, by using queryset to define a filtered list of objects you can 
    be more specific about the objects that will be visible in the view (see Making queries for 
    more information about QuerySet objects, and see the class-based views reference for the complete details)."""

class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'
