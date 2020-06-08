from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_details.html'
