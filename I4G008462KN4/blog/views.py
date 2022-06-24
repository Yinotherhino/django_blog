from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

# Create your views here.

class PostListView(ListView):
    model = Post
class PostCreateView(ListView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
class PostDetailView(ListView):
    model = Post
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")