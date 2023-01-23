from django.urls import path
from .views import show_login

urlpatterns = [
    path("login/", show_login, name="login")
]
