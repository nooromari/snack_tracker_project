from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Snack
# Create your views here.

class SnackDetail(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
