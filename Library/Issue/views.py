from typing import Generic
from django.db import models
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Issue.models import book, issueBook
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

class IssueBookShow(ListView):
    model = issueBook
    context_object_name = 'booklist'

class BookShow(ListView):
    model = book
    context_object_name = 'books'
    template_name = 'Issue/index.html'

class addBook(CreateView):
    model = book
    fields ='__all__'
    success_url = reverse_lazy('addbook')
    template_name = 'Issue/addbook.html'

class bookdetails(DetailView):
    model = book
    context_object_name = 'book'
    template_name = 'Issue/bookdetails.html'