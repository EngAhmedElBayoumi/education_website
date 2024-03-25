from . import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path("blog/", views.blog, name="blog"),
    path("blog_detail/<int:id>/", views.blog_detail, name="blog_detail"),
    path("search/", views.search, name="search"),
]