from django.urls import path
from .views import PostListView, PostDetailView, NewPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/<uuid:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", NewPostView.as_view(), name="new-post"),
    path("post/<uuid:pk>/edit/", UpdatePostView.as_view(), name="update-post"),
    path("post/<uuid:pk>/delete/", DeletePostView.as_view(), name="delete-post"),
]
