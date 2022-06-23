from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('app:author-detail', kwargs={'pk': int(self.id)})

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Language(models.Model):
    name = models.CharField(max_length=100)


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=100)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)