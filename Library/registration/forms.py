from django import forms
from django.db.models.base import Model
from django.forms import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrViewForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.IntegerField()
    class Meta:
        model = User
        fields = ('name', 'email', 'username', 'password', 'phone')

        widgets = {
            'password': forms.PasswordInput()
        }