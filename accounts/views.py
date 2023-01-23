from django.shortcuts import render, redirect
from .forms import LogInForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def create_user(request):
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data["username"]
            password = signup_form.cleaned_data["password"]
            password_confirmation = signup_form.cleaned_data["password_confirmation"]
            if password != password_confirmation:
                return "the passwords do not match"
            User.objects.create_user(username, password=password)
            return redirect("list_projects")
    else:
        signup_form = SignUpForm()
    context = {
        "signup_form": signup_form
    }
    return render(request, "accounts/signup.html", context)
# Create a user account based off username and passwords being less than 150
# characters if the password meets requirements then new user is created
# and redirected to home page


def show_login(request):
    if request.method == "POST":
        login_form = LogInForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        login_form = LogInForm()
    context = {"login_form": login_form}
    return render(request, "accounts/login.html", context)
# Will show the form for pre-registered users to login


def logout_user(request):
    logout(request)
    return redirect("login")
# Logs out the current user
