from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('recommended_posts/', views.PostListRecommended.as_view()),
    path('post-details/<int:pk>', views.PostDetail.as_view()),
    path('comments/<int:pk>', views.CommentList.as_view()),
    path('comments-post/', views.CommentPost.as_view()),
    # path('view-add/', views.ViewAdd.as_view()) <-- disabled in views.py
]
