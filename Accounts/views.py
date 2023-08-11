# app_auth/views.py

from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserAccountForm
import Accounts.models
from Accounts.forms import RegisterUserForm




UserModel = get_user_model()

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


# @login_required(login_url=reverse_lazy('login'))
# class AccountView(views.UpdateView):


@login_required
def view_and_edit_account(request):
    user = request.user

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('account')
    else:
        form = UserAccountForm(instance=user)

    return render(request, 'account', {'form': form})