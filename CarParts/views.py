from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView
from CarParts.models import Tyre
from CarParts.forms import ContactForm
from django import forms


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
            from_email=form.cleaned_data['from_email'],
            recipient_list=[form.cleaned_data['email']],
        )
        return super().form_valid(form)
