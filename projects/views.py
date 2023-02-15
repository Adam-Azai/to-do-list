from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import CreateProjectForm


@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {"list_projects": list_projects}
    return render(request, "projects/list.html", context)


# if a user is logged in, they will be able to see the projects
# they have created


@login_required
def project_details(request, id):
    project = Project.objects.get(id=id)
    context = {"project": project}
    return render(request, "projects/detail.html", context)


# shows the project at a specified id with the tasks that are included in it


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()
    context = {"form": form}
    return render(request, "projects/create.html", context)


def view_contactus(request):
    return render(request, "projects/contact.html")

# @login_required
# def gantt_chart_tasks(request):
#     qs = Task.objects.all()
#     task_data = [
#         {
#             "Task": x.name,
#             "Start": x.start_date,
#             "End": x.due_date,
#             "Responsible": x.assignee.username
#         } for x in qs
#     ]
#     df = pd.DataFrame(task_data)

#     fig = px.timeline(
#         df, x_start="Start", x_end="End", y="Task", color="Responsible"
#     )
#     fig.update_yaxes(autorange="reversed")
#     gantt_plot = plot(fig, output_type="div")
#     context = {'plot_div': gantt_plot}
#     return render(request, "projects/chart.html", context)
