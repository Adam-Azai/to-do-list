from django.db import models


class LogIn(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)


class SignUp(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    password_confirmation = models.CharField(max_length=150)
