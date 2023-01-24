from django.urls import path
from .views import list_projects, project_details, create_project

urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", project_details, name="show_project"),
    path("create/", create_project, name="create_project"),
]
