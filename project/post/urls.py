from django.urls import path
from . import views


app_name = "post"
urlpatterns = [
    path("", views.home, name="index"),
    path("post_list/", views.post_list, name="post_list"),
    path("post_detail/<int:id>/", views.post_detail, name="post_detail"),
    path("create_post/", views.create_post, name="create_post"),
    path("post_vote/<int:id>/", views.post_vote, name="post_vote"),
    path("comments_vote/<int:id>/", views.comment_vote, name="comment_post"),
]
