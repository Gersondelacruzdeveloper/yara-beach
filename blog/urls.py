from django.urls import path
from . import views
from .views import (
    BlogPostDetailView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)


urlpatterns = [
  path('', views.blog_post_list, name='blog_post_list'),  # This matches 'blog/'.
    path('<slug:slug>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('<slug:slug>/update/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]
