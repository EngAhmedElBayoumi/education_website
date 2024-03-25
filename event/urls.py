from . import views
from django.urls import path

app_name = "event"

urlpatterns = [
    path("event/", views.event, name="event"),
    path("event_detail/<int:id>/", views.event_detail, name="event_detail"),
    path("search/", views.search, name="search"),
]