from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', views.PaymentView.as_view(), name='pay'),
    path("payment-cancelled", TemplateView.as_view(template_name="payment-cancelled.html")),
    path("payment-succeeded", TemplateView.as_view(template_name="payment-succeeded.html")),
    path("create-paypal-order", views.CreatePaypalOrderView.as_view(), name="create-paypal-order"),
    path("capture-paypal-order", views.CaptureFundView.as_view(), name="capture-paypal-order"),
    ]