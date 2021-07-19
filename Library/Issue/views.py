import re
from django.contrib.auth.models import User
from django.http import request
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Issue.models import book, issueBook
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import book, issueBook
# from Issue.forms import Addform
# Create your views here.


class dashboard(ListView):
    model = issueBook
    context_object_name = 'booklist'
    template_name = 'Issue/dashboard.html'

    def get_queryset(self):
        return issueBook.objects.filter(user=self.request.user)


class BookShow(ListView):
    model = book
    context_object_name = 'books'
    template_name = 'Issue/index.html'


class addBook(CreateView):
    model = book
    fields = '__all__'
    success_url = reverse_lazy('addbook')
    template_name = 'Issue/addbook.html'


class bookdetails(DetailView):
    model = book
    context_object_name = 'book'
    template_name = 'Issue/bookdetails.html'


class show(View):

    def get(self, request,*args, **kwargs):
        user = request.user
        print(user)

        books = request.GET.get['book_id']
        print(books)

# class BookIssueView(CreateView):
#     model = issueBook
#     # form_class = Addform
#     context_object_name = 'book'
#     template_name = 'Issue/issuebook.html'
#     success_url = reverse_lazy('dashboard')

    # def get_queryset(self):
    #     user = User.objects.get(username= self.request.user)
    #     b = book.objects.get(bookname = self.request)

    #     obj = issueBook(user=user,bookname=b)
    #     obj.save()
        
