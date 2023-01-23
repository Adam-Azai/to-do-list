from django.forms import ModelForm, PasswordInput
from accounts.models import LogIn, SignUp


class LogInForm(ModelForm):
    class Meta:
        model = LogIn
        fields = [
            "username",
            "password",
        ]
        widgets = {"password": PasswordInput}


# Display Login Form with username and password input boxes


class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = [
            "username",
            "password",
            "password_confirmation",
        ]
        widgets = {
            "password": PasswordInput,
            "password_confirmation": PasswordInput,
        }
