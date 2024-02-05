from django.shortcuts import render
from projects.models import Project

# Create your views here.


def show_project_model(request):
  model_list = Project.objects.all()
  context = {
    "model_list": model_list
  }
  return render(request, "projects/list_projects.html", context)
