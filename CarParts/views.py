import json

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, FormView
from CarParts.models import Tyre
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from CarParts.forms import ContactForm
from django import forms
from django.urls import reverse_lazy
from django.conf import settings

from Cart.models import Order, OrderItem


# Create your views here.

# class Test(TemplateView):
#     template_name = 'test.html'

class TyreListView(ListView):
    model = Tyre
    template_name = 'list-parts.html'
    context_object_name = 'tyres'
    ordering = ['-id']
    paginate_by = 3
    tyres = Tyre.objects.all()


class TyreDetailView(DetailView):
    model = Tyre
    template_name = 'detail-parts.html'
    context_object_name = 'tire'
    id = 'tyre_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tyres'] = Tyre.objects.all()
        return context

    def get_queryset(self):
        return Tyre.objects.all()

    def get_object(self, queryset=None):
        return Tyre.objects.get(id=self.kwargs['pk'])

def contact_view(request):

    if request.method == 'POST':

        form = ContactForm()

        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['from_email'],
                recipient_list=[form.cleaned_data['email']],
            )

    form = ContactForm()

    return render(request, 'contact_form.html', {"form": form})

class ContactFormView(FormView):

    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        send_mail(
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message'],
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[form.cleaned_data['email']],
        )
        return super().form_valid(form)

class TermsAndConditionsView(TemplateView):
    template_name = 'terms-and-conditions.html'


@csrf_exempt
def updateItem(request):

    print("updateItem")

    data = json.loads(request.body)
    # all_data = cartData(request)

    print(data)
    # print(all_data)

    action = data['action']
    # quantity = all_data['order']['get_cart_items']
    quantity = data['quantity']

    print("QUANTITY")
    print(quantity)

    tyre_id = int(data['productId'])
    print("Tyre id -----------")
    print(tyre_id)

    tyre = Tyre.objects.get(id=tyre_id)

    print('Action:', action)
    print('Product:', tyre)
    print('Quantity:', quantity)

    order, created = Order.objects.get_or_create(customer=request.user, status="DRAFT")
    print(order)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=tyre)

    print(action)

    print(orderItem.id, created)

    if action == 'delete':
        orderItem.delete()

    if action == "remove" or action == "add" or action == "plus":
        orderItem.quantity += int(quantity)
        orderItem.save()

    if action == 'remove':
        if orderItem.quantity <= 0:
            orderItem.delete()

    print(action, orderItem.quantity)

    return JsonResponse({"message": "ok"})
