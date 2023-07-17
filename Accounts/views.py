from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.views import RegisterView

# Create your views here.

class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

# class RegisterView(RegisterView):
#     template_name = 'register.html'
#     redirect_authenticated_user = True

class SignOutView(LogoutView):
    template_name = 'logout.html'
    redirect_authenticated_user = True