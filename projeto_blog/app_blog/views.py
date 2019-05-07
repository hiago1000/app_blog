from django.shortcuts import render
from .models import Postagem
from django.views.generic import ListView, TemplateView, FormView

# Create your views here.
class HomePageView(ListView):
    model=Postagem
    template_name='app_blog/home.html'