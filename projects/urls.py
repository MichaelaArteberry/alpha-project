from django.urls import path
from projects.views import show_project_model, show_projects, create_project



urlpatterns = [
    path("", show_project_model, name="list_projects"),
    path("<int:id>", show_projects, name="show_project"),
    path("create/", create_project, name="create_project"),
]
