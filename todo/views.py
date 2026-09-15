from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")

    return render(request, "todo/task_list.html", {
        "tasks": tasks
    })


def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        category = request.POST.get("category")
        starred = request.POST.get("starred") == "on"

        Task.objects.create(
            title=title,
            description=description,
            category=category,
            starred=starred
        )

        return redirect("task_list")

    return render(request, "todo/add_task.html")


def toggle_star(request, task_id):
    task = Task.objects.get(id=task_id)

    task.starred = not task.starred
    task.save()

    return redirect("task_list")