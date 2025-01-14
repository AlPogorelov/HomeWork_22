from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from .forms import UserCreationForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')


class RegisterView(View):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')
