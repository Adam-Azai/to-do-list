from django.db import models
from projects.models import Project
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    week_number = models.CharField(blank=True, max_length=2)
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project, related_name=("tasks"), on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        User, related_name=("tasks"), on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} {self.start_date} {self.due_date} {self.project} {self.assignee}"

    def save(self, *args, **kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1]
            super().save(*args, **kwargs)
