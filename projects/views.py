from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required


@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {"list_projects": list_projects}
    return render(request, "projects/list.html", context)


# if a user is logged in, they will be able to see the projects
# they have created
