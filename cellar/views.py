from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bottle
# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Bottle
    context_object_name = 'cellar'

class WineDetailView(DetailView):
    template_name = 'wine_detail.html'
    model = Bottle
