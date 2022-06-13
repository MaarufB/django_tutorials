from django.contrib import admin
from .models import (Movie, Blog, Book, Author, Project)
# Register your models here.

admin.site.register([Movie, Blog, Book, Author, Project])