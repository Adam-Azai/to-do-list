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
    context = {
        "project": project
    }
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
    context = {
        "form": form
    }
    return render(request, "projects/create.html", context)
