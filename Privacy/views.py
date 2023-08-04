from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PrivacyView(TemplateView):

    template_name = 'privacy.html'
