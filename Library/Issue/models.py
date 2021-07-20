from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class book(models.Model):
    bookname = models.CharField(max_length=200)
    authername = models.CharField(max_length=200)

    def __str__(self):
        return self.bookname


class issueBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookname = models.ForeignKey(book, on_delete=models.CASCADE)
    issuingDate = models.DateTimeField(auto_now_add=True)
