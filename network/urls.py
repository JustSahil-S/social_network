
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("posts", views.posts, name="posts"),
    path("profile/<str:user>", views.profile, name="profile"),
    path("likePosts/<int:id>", views.likePosts, name="likePosts"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("follow/<str:user>", views.follow, name="follow"),
    path("following", views.follow_page, name="follow_page"),
    ]
