from django.urls import path
from projects.views import show_project_model, show_projects



urlpatterns = [
    path("", show_project_model, name="list_projects"),
    path("<int:id>", show_projects, name="show_project"),
]
