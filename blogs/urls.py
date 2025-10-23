from django.urls import path
from .views import PostList, PostDetail  # , post_detail

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("blog/<uuid:pk>/", PostDetail.as_view(), name="post-detail"),
]
