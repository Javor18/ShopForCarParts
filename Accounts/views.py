from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.urls import reverse_lazy
# from Accounts.forms import RegistrationForm
# Create your views here.

class RegisterView(FormView):
    template_name = 'register.html'
    # form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

# class RegisterView(RegisterView):
#     template_name = 'register.html'
#     redirect_authenticated_user = True

class SignOutView(LogoutView):
    template_name = 'logout.html'
    redirect_authenticated_user = True