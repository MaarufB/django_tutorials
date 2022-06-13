from django.contrib import admin
from .models import (Author, Blog, Entry, Publication, Article)
# Register your models here.

admin.site.register([
    Author,
    Blog,
    Entry,
    Article,
    Publication
])


