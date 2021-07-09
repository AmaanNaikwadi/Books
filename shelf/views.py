from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from shelf.models import Book
from django.http import JsonResponse
import re
from django.http import HttpResponse, HttpResponseRedirect
import json

def home(request):
    if request.method == "GET":
        return render(request, 'shelf/home.html')
    else:
        name=request.POST.get('name')
        author=request.POST.get('author')
        language=request.POST.get('language')
        genre=request.POST.get('genre')
        try:
            book = Book.objects.get(name=name)
            return render(request, 'shelf/home.html', {'message': 'The book is already present.'})
        except Book.DoesNotExist:
            book = Book(name=name, author=author, language=language, genre=genre)
            book.save()
            return render(request, 'shelf/home.html', {'message': 'Book has been added Successfully.'})

def display(request):
    if request.method == "GET":
        book = Book.objects.all()
        return render(request, 'shelf/display.html', {'books': book})
    else:
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



            


