from django.urls import path
from .views import create_task, view_tasks, edit_tasks

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", view_tasks, name="show_my_tasks"),
    path('edit/<int:id>', edit_tasks, name="edit_tasks"),
]
