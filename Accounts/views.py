from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic as views
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views

class RegisterUserView(views.CreateView):
    template_name = 'register.html'
    form_class = auth_forms.UserCreationForm

    def post(self, request, *args, **kwargs):
