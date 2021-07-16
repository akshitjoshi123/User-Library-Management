from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserRegistrViewForm

# from .forms import userForm
# Create your views here.

# class AdminLogin(LoginView):
#     template_name = 'Login.html'


class UserRegistrView(CreateView):

    form_class = UserRegistrViewForm
    # form_class = userForm
    template_name = 'register/registration.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegistrView, self).form_valid(form)


class UserLoginView(LoginView):
    # form_class = AuthenticationForm
    # authentication_form = None
    template_name = 'register/login.html'
    redirect_authenticated_user = True
    # extra_context = None
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('bookshow')
