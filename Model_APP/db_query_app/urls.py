from django.urls import path
from . import views
#include app_name

urlpatterns = [
    # add url endpoints here!
    path("", views.entry_list, name="entry-list"),
]


