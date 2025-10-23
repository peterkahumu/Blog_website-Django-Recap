from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = "posts/home.html"


class PostDetail(DetailView):
    model = Post
    template_name = "posts/post_detail.html"


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'posts/post_detail.html', {'post': post})
