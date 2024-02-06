from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def show_project_model(request):
  project_list = Project.objects.filter(owner=request.user)
  context = {
    "project_list": project_list
  }
  return render(request, "projects/list_projects.html", context)





@login_required
def show_projects(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project_object": project,
    }
    return render(request, "projects/projectdetail.html", context)
