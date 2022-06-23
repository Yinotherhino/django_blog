from django.shortcuts import render

# Create your views here.

class PostListView(ListView):
    model = Post
class PostCreateView(ListView):
    model = Post
    fields = "__all__"
    success_url = reverse("blog:all")
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