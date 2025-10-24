from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.
class PostListView(ListView):
    """List all the posts in the database."""
    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    """List a specific post using the primary key."""
    model = Post
    template_name = "posts/post_detail.html"

