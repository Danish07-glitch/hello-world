from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView
from blog.models import Post


# Create your views here.

class IndexView(TemplateView):
    model=Post
    template_name='base.html'

class BlogListView(ListView):
    model=Post
    template_name='home.html'

class BlogDetailView(DetailView):
    model=Post
    template_name='post_detail.html'
