from django.urls import path
from .views import BookShow, addBook, bookdetails,show,dashboard

urlpatterns = [
    path('', BookShow.as_view(), name='bookshow'),
    path('dashboard', dashboard.as_view(), name='dashboard'),
    path('addbook', addBook.as_view(), name='addbook'),
    path('bookdetails/<int:pk>/', bookdetails.as_view(), name='bookdetails'),
    path('issuebook/<int:book_id>/', show.as_view(), name='issuebook')

]
