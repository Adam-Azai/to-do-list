from django.urls import path
from .views import show_login, logout_user

urlpatterns = [
    path("login/", show_login, name="login"),
    path("logout/", logout_user, name="logout"),
]
