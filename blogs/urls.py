from django.urls import path
from .views import PostListView, PostDetailView, NewPostView

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/<uuid:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", NewPostView.as_view(), name='new-post'),
]
