from django.forms import BooleanField
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, authenticate, login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django import forms

class RegisterUserForm(auth_forms.UserCreationForm):
    content = BooleanField()

    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'It works!'

class RegisterUserView(views.CreateView):
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

class LoginUserView(auth_views.LoginView):

    template_name = 'login.html'

