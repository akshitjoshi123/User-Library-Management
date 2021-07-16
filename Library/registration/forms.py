from django import forms
from django.contrib.auth.models import User


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
