from . import views
from django.urls import path

app_name = "courses"

urlpatterns = [
    path("courses/", views.courses, name="courses"),
    path("course_detail/<int:id>/", views.course_detail, name="course_detail"),
    path("search/", views.search, name="search"),
    
]