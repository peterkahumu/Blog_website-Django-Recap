from django.urls import path
from .views import PostListView, PostDetailView  # , post_detail

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("blog/<uuid:pk>/", PostDetailView.as_view(), name="post-detail"),
]
