from django.shortcuts import render
from django.views.generic import ListView
from news.models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'home.html'