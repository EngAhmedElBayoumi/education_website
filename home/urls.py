from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("error_404/", views.error_404, name="error_404"),
    path("error_500/", views.error_500, name="error_500"),
    
]
    