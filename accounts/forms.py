from django.forms import ModelForm, PasswordInput
from accounts.models import LogIn


class LogInForm(ModelForm):
    class Meta:
        model = LogIn
        fields = [
            "username",
            "password",
        ]
        widgets = {"password": PasswordInput}
