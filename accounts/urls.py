from . import views
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path("log_in/", views.log_in, name="login"),
    path("log_out/", views.log_out, name="logout"),
    path("sign_up/", views.sign_up, name="signup"),
    path("profile/", views.profile, name="profile"),
]