from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from Issue.models import book, issueBook
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect


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
    def get(self, request, book_id, *args, **kwargs):
        user = request.user
        books = book.objects.get(id=book_id)
        obj = issueBook(user=user, bookname=books)
        obj.save()
        return redirect('/dashboard')

