from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import CreateTaskForm
from .models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm()
    context = {"form": form}
    return render(request, "tasks/create.html", context)


@login_required
def view_tasks(request):
    view_task = Task.objects.filter(assignee=request.user)
    context = {"view_task": view_task}
    return render(request, "tasks/mine.html", context)
