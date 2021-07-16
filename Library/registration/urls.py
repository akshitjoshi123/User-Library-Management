from django.urls import path, include
from registration.views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

urlpatterns = [
    # path('login/', AdminLogin.as_view(), name="login")
    path('register/', UserRegistrView.as_view(), name='register'),
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),

]
