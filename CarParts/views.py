from django.shortcuts import render
from django.views.generic import ListView, DetailView
from CarParts.models import Tires

# Create your views here.


class TyreListView(ListView):
    model = Tires
    template_name = 'list-parts.html'
    context_object_name = 'tyres'
    ordering = ['-id']

class TyreDetailView(DetailView):
    model = Tires
    template_name = 'detail-tyres.html'
    context_object_name = 'tyre'