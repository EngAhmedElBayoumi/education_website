from . import views
from django.urls import path

app_name = "book"

urlpatterns = [
    path("book/", views.book, name="book"),
    path("search/", views.search, name="search"),
]