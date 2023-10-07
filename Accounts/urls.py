"""
URL configuration for CarShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Accounts import views


urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register_user'),
    path('login/', views.LoginUserView.as_view(), name='login_user'),
    path('logout/', views.LogoutUserView.as_view(), name='logout_user'),
    path('', views.UsersListView.as_view(), name='users_list'),
    path('accounts/', views.view_and_edit_account, name='account'),
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('add-to-wishlist/<int:wishlist_item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
