from django.shortcuts import render, redirect
from .forms import LogInForm
from django.contrib.auth import authenticate, login, logout


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
