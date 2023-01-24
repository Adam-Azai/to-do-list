from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        User, related_name=("projects"), on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.name}"
