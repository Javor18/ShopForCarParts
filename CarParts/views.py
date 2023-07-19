from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from CarParts.models import Tires

# Create your views here.

# class Test(TemplateView):
#     template_name = 'test.html'

class TyreListView(ListView):
    model = Tires
    template_name = 'list-parts.html'
    context_object_name = 'tyres'
    ordering = ['-id']
    paginate_by = 2

class TyreDetailView(DetailView):
    model = Tires
    template_name = 'detail-tyres.html'
    context_object_name = 'tyre'