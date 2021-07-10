from django.db import models
from django.contrib.auth.models import User, auth

class Book(models.Model):
    name=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    language=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    book_id = models.CharField(max_length=1000)
    details=models.TextField()

    def __str__(self):
        return self.name



