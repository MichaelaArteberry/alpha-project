from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task


# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form":form,
    }

    return render(request, "tasks/create_task.html", context)




@login_required
def list_tasks(request):
    task_list = Task.objects.filter(assignee=request.user)
    context = {
        "tasks_list": task_list
    }

    return render(request, "tasks/my_tasks.html", context)
