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
from CarParts import views
from django.urls import include

urlpatterns = [
    path('', views.TyreListView.as_view(), name='main'),
    # path('tyres/<str:name>', views.TyreDetailView.as_view(), name='tyre_detail'),
    path('tyres/<int:pk>', views.TyreDetailView.as_view(), name='tyre_detail'),
    path('contact-us/', views.contact_view, name='contact'),
]