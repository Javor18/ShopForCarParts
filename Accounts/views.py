# app_auth/views.py

from django import forms

from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _
from django.forms import CharField, PasswordInput, BooleanField
# from django import allowed_users
from django.contrib.auth.models import Group, User

from CarParts.models import Profile
from CarParts.signals import send_successfull_registration_email

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    content = BooleanField()

    password2 = CharField(
        label="Repeat Password",
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        instance = super(RegisterUserForm, self).save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance

# def register_view(request):
#     if request.method == 'GET':
#         form = RegisterUserForm()
#     else:
#         form = RegisterUserForm(request.POST, initial, instance, data)
#
#         if form.is_valid():
#             # form_valid(form)
#             form.save()
#             # redirect ...
#         # redirect ...
#     # ....

class RegisterUserView(views.CreateView):
    template_name = 'register.html'
    form_class = RegisterUserForm

    # Static way of providing `success_url`
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        result = super().form_valid(form)

        # send_successfull_registration_email(None)

        login(self.request, self.object)

        return result

    # def get_form_class(self):
    #     if condition1:
    #         return Condition1Form
    #     elif condition2:
    #         return Condition2Form
    #     else:
    #         return Condition3Form

    # Dynamic way of providing `success_url`
    # def get_success_url(self):
    #     pass


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['initial'] = {
            'password': '210810Skydrive'
        }

        return kwargs


class LogoutUserView(auth_views.LogoutView):
    pass


UserModel = get_user_model()


@login_required
def func_view(request):
    pass


class ViewWithPermission(auth_mixins.PermissionRequiredMixin, views.TemplateView):
    template_name = 'users_list.html'


class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'users_list.html'

    # Login URL only for this view:
    # login_url = 'custom-login/url'


@login_required(login_url=reverse_lazy('login'))
class AccountView(views.UpdateView):

    model = UserModel
