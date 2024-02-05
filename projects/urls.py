from django.urls import path
from projects.views import show_project_model



urlpatterns = [
    path("projects/", show_project_model, name="list_projects"),
]
