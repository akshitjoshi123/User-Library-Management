from Issue.models import book
from django.contrib.auth import views
from django.urls import path, include
from .views import BookShow, IssueBookShow, addBook, bookdetails

urlpatterns = [
    path('',BookShow.as_view(), name='bookshow'),
    path('issuebook',IssueBookShow.as_view(), name='issuebook'),
    path('addbook', addBook.as_view(), name='addbook'),
    path('bookdetails/<int:pk>', bookdetails.as_view(), name='bookdetails')
    
]
