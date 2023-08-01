from django.forms import BooleanField
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, authenticate, login, get_user_model
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth import mixins as auth_mixins

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

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #
    #     kwargs['initial'] = {
    #         'password': '210810Skydrive@',
    #     }
    #
    #     return kwargs


UserModel = get_user_model()

class ViewWthPermission(auth_mixins.PermissionRequiredMixin, views.TemplateView):
    template_name = 'users_list.html'

class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'users_list.html'
    model = UserModel


class LogoutUserView(auth_views.LogoutView):
    pass