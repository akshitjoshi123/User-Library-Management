from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
# Create your models here.

class issueBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.CharField(max_length=200)
    issuingDate =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book


class book(models.Model):
    bookname = models.CharField(max_length=200)
    authername = models.CharField(max_length=200)
    def __str__(self):
        return self.bookname
