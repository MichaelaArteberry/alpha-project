from django.shortcuts import render
from projects.models import Project

# Create your views here.


def show_project_model(request):
  project_list = Project.objects.all()
  context = {
    "project_list": project_list
  }
  return render(request, "projects/list_projects.html", context)
