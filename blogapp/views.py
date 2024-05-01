from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'



