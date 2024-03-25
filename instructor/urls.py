#path
from django.urls import path    
from . import views

app_name="instructor"

urlpatterns = [
    path('instructors/', views.instructor, name='instructor'),
    path('instructor/<int:id>/', views.instructor_detail, name='instructor_detail'),
    path('search/', views.search, name='search'),
]