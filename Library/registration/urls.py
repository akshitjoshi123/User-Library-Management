from django.urls import path
from registration.views import UserLoginView, UserRegistrView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('login/', AdminLogin.as_view(), name="login")
    path('register/', UserRegistrView.as_view(), name='register'),
    path('', UserLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),

]
