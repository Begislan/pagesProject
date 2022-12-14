from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

# Create your views here.
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView():
    model = Post
    template_name = 'post_new.html'

