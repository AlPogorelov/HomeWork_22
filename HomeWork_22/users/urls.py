from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView

from .apps import UsersConfig

app_name = UsersConfig

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),


]

