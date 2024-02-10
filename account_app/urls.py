from . import views
from django.urls import path

app_name = "account_app"
urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("about", views.about, name="about"),
]
