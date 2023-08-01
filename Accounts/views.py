from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import BooleanField
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, resolve_url
from django.utils.decorators import method_decorator
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, authenticate, login, get_user_model
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth import mixins as auth_mixins
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from CarParts.models import Profile

# Create your views here.

from CarShop import settings

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    content = BooleanField()

    first_name = forms.CharField(
        max_length=30,
        required=True
    )

    password2 = forms.CharField(
        label= "Repeat Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        # help_text= "Repeat password, please",
        help_text= None,
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['password1'].help_text = _("It works!")
        self.fields['password1'].help_text = None
    def save(self, commit=True):
        user = super().save(commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user,
        )
        if commit:
            profile.save()

        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

class RegisterUserView(views.CreateView):
    template_name = 'register.html'
    form_class = RegisterUserForm

    # Static way of providing `success_url`
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['initial'] = {
            'password': '210810Skydrive@',
        }

        return kwargs

@login_required
def func_view(request):
    pass

class ViewWithPermission(auth_mixins.PermissionRequiredMixin, views.TemplateView):
    template_name = 'users_list.html'


class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'users_list.html'


class LogoutUserView(auth_views.LogoutView):
    pass