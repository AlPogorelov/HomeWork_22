from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserRegisterView, custom_logout

from .apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', custom_logout, name='logout'),

]

