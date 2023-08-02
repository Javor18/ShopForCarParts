from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from CarParts.models import Tyre

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


