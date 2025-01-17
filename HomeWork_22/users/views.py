from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, get_user_model
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from .forms import UserCreationForm, UserRegisterForm
from .models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:product_list')


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:login')


def custom_logout(request):
    logout(request)
    return redirect('/catalog/')
