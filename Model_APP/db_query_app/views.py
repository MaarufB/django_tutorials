from django.shortcuts import render
from django.db.models import Q
from .models import Author, Entry, Blog
from django.http import JsonResponse, HttpResponse
from .api.serializers import AuthorSerializer, EntrySerializer, BlogSerializer

# Create your views here.


def entry_list(request):
    blogs = Blog.objects.all()
    authors = Author.objects.all()
    entries = Entry.objects.all()

    blogs_serializer = BlogSerializer(blogs, many=True)
    authors_serializer = AuthorSerializer(authors, many=True)
    entries_serializer = EntrySerializer(entries, many=True)

    context = {
        "blogs": blogs_serializer.data,
        "authors": authors_serializer.data,
        "entries": entries_serializer.data,
    }

    return JsonResponse(context)