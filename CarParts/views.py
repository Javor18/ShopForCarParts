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
    paginate_by = 3
    # tyre_detail = 'tyre_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tyres'] = Tires.objects.all()
        return context

    def get_queryset(self):
        return Tires.objects.all()

    def get_object(self, queryset=None):
        return Tires.objects.get(id=self.kwargs['pk'])

class TyreDetailView(DetailView):
    model = Tires
    template_name = 'detail-parts.html'
    context_object_name = 'tyre'
    id = 'tyre_id'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tyres'] = Tires.objects.all()
    #     return context
    #
    # def get_queryset(self):
    #     return Tires.objects.all()
    #
    # def get_object(self, queryset=None):
    #     return Tires.objects.get(id=self.kwargs['pk'])


