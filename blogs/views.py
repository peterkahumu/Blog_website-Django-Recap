from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Post


# Create your views here.
class PostListView(ListView):
    """List all the posts in the database."""

    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"
    ordering = "-created_at"


class PostDetailView(DetailView):
    """List a specific post using the primary key."""

    model = Post
    template_name = "posts/post_detail.html"


class NewPostView(CreateView):
    model = Post
    template_name = "posts/create_post.html"
    fields = ["title", "author", "body"]


class UpdatePostView(UpdateView):
    model = Post
    template_name = "posts/edit_post.html"
    fields = ["title", "body"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy("home")
