from typing import ValuesView
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from shelf.models import Book
from django.http import JsonResponse
import re
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.views.generic.detail import DetailView

class home(DetailView):

    def get(self, request, *args, **kwargs):
        return render(request, 'shelf/home.html')

    def post(self, request, *args, **kwargs):
        name=request.POST.get('name')
        author=request.POST.get('author')
        language=request.POST.get('language')
        genre=request.POST.get('genre')
        details=request.POST.get('details')
        book_info = [name, author, language, genre]
        book_id = "_".join(book_info)
        book_id = '_'.join(book_id.split())
        try:
            book = Book.objects.get(name=name, author=author, language=language, genre=genre)
            return render(request, 'shelf/home.html', {'message': 'The book is already present.'})
        except Book.DoesNotExist:
            book = Book(name=name, author=author, language=language, genre=genre, book_id=book_id, details=details)
            book.save()
            return render(request, 'shelf/home.html', {'message': 'Book has been added Successfully.'})

class display(DetailView):
    
    def get(self, request, *args, **kwargs):
        book = Book.objects.all()
        return render(request, 'shelf/display.html', {'books': book})

    def post(self, request, *args, **kwargs):
        language = request.POST.getlist('Language')
        genre = request.POST.getlist('Genre')
        for i in range (0, len(genre)):
            language.append(genre[i])
        filters = json.dumps(language)
        book = Book.objects.filter(language__in=language)
        book1 = Book.objects.filter(genre__in=genre)
        matches = book.union(book1)
        count = matches.count()
        return render(request, 'shelf/display.html', {'message': count, 'books': matches, 'filters': filters})

class detail(DetailView):

    def post(self, request, *args, **kwargs):
        name = request.POST.get("book")
        book = Book.objects.get(book_id=name)
        return render(request, 'shelf/detail.html', {'book': book})



            


