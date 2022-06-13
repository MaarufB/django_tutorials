from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'members'

urlpatterns = [
    path('',views.index, name='index'),
    path('add_view/', views.add_view, name='add_view'),
    path('add_member/', views.add_member, name='add_member'),
    path('api/get_members/', views.get_members, name='get_members'),
    path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),
    # path('update_member_view/<int:member_id>/', views.update_member_view, 'update_member_view'),
    path('update_view/<int:member_id>/', views.update_view, name='update_view'),
    path('update_view/update_member/<int:member_id>', views.update_member, name='update_member'),
]