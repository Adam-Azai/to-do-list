from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import CreateTaskForm
from .models import Task
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from tasks.models import Task




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
    qs = Task.objects.all()
    task_data = [
        {
            "Task": x.name,
            "Start": x.start_date,
            "End": x.due_date,
            "Responsible": x.assignee.username
        } for x in qs
    ]
    df = pd.DataFrame(task_data)

    fig = px.timeline(
        df, x_start="Start", x_end="End", y="Task", color="Responsible"
    )
    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")
    context = {"view_task": view_task, "plot_div": gantt_plot}
    return render(request, "tasks/mine.html", context)



@login_required
def edit_tasks(request, id):
    edit = Task.objects.get(id=id)
    if request.method == "POST":
        editform = CreateTaskForm(request.POST, instance=edit)
        if editform.is_valid():
            edit = editform.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect("show_my_tasks")
    else:
        editform = CreateTaskForm(instance=edit)
    context = {
        "editform": editform}
    return render(request, "tasks/edit.html", context)
