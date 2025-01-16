from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from .forms import UserCreationForm
from .models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:product_list')


class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')


def custom_logout(request):
    logout(request)
    return redirect('/catalog/')
