from re import template
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
# from .models import *
from .views import *

urlpatterns = [
    path('', TaskList.as_view(template_name='base/tasks.html'), name='index'),
    # path('create-task/',MyFormView.as_view(), name='create-task'),
    # path('create-task/<int:id>/',MyFormView.as_view(), name='create-task'),
    path('upsert/', TaskUpsertView.as_view(), name='upsert'),
    path('upsert/<int:id>/', TaskUpsertView.as_view(), name='upsert'),
    #This is an example on how to use generic view an add it on url
    path('publishers/', PublisherListView.as_view()),
    path('publisher/', PublisherDetailView.as_view()),
    path('book/', BookList.as_view()),
]

"""
when using a decorator used this example

urlpatterns = [
    path('about/', login_required(TemplateView.as_view(template_name="secret.html"))),
    path('vote/', permission_required('polls.can_vote')(VoteView.as_view())),
]

"""