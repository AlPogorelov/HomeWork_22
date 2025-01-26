from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, get_user_model, login
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from .forms import UserCreationForm, UserRegisterForm
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.core.cache import cache


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        cache.delete('product_list')
        return super().form_valid(form)


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)


    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


def custom_logout(request):
    cache.delete('product_list')
    logout(request)
    return redirect('/catalog/')
