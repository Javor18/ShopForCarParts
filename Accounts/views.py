# app_auth/views.py

from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib import messages
from .forms import UserAccountForm
from Accounts.forms import RegisterUserForm
from django.shortcuts import render, redirect, get_object_or_404
from Accounts.models import WishlistItem
from CarParts.models import Tyre




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

    return render(request, 'account.html', {'form': form})

@login_required
def view_wishlist(request):

    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    product = Tyre.objects.get(pk=product_id)
    wishlist, created = WishlistItem.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect('list-parts')  # Change to your product list view

@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_item_id, user=request.user)
    wishlist_item.delete()
    return redirect('wishlist')