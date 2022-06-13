from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_name/', views.get_name, name='get_name'),
    path('contact_me/', views.contact_me, name='contact_me'),
    path('create_project/', views.createProject, name='create_project'),
    path('get_projects/', views.get_projects, name="get_projects"),
    path('update_project/<str:pk>/', views.update_project, name="update_project"),
    path('delete_project/<str:pk>/', views.delete_project, name="delete_project"),

]