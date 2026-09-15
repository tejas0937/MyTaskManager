from django.shortcuts import get_object_or_404, redirect, render

from .models import Task


def task_list(request):

    tasks = Task.objects.all().order_by("-created_at")

    current_filter = request.GET.get("filter", "all")

    if current_filter == "starred":
        tasks = tasks.filter(starred=True)

    elif current_filter == "completed":
        tasks = tasks.filter(completed=True)

    elif current_filter == "pending":
        tasks = tasks.filter(completed=False)

    elif current_filter in [
        "Self",
        "Work",
        "Study",
        "Personal",
        "Other",
    ]:
        tasks = tasks.filter(category=current_filter)

    all_tasks = Task.objects.all()

    context = {
        "tasks": tasks,
        "current_filter": current_filter,

        "total_tasks": all_tasks.count(),

        "completed_tasks": all_tasks.filter(
            completed=True
        ).count(),

        "pending_tasks": all_tasks.filter(
            completed=False
        ).count(),

        "starred_tasks": all_tasks.filter(
            starred=True
        ).count(),
    }

    return render(
        request,
        "todo/task_list.html",
        context
    )


def add_task(request):

    if request.method == "POST":

        title = request.POST.get("title", "").strip()

        description = request.POST.get(
            "description",
            ""
        ).strip()

        category = request.POST.get(
            "category",
            "Other"
        )

        starred = request.POST.get(
            "starred"
        ) == "on"

        if title:

            Task.objects.create(
                title=title,
                description=description,
                category=category,
                starred=starred,
            )

            return redirect("task_list")

    return render(
        request,
        "todo/add_task.html"
    )


def edit_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id
    )

    if request.method == "POST":

        title = request.POST.get(
            "title",
            ""
        ).strip()

        description = request.POST.get(
            "description",
            ""
        ).strip()

        category = request.POST.get(
            "category",
            "Other"
        )

        starred = request.POST.get(
            "starred"
        ) == "on"

        if title:

            task.title = title
            task.description = description
            task.category = category
            task.starred = starred

            task.save()

            return redirect("task_list")

    return render(
        request,
        "todo/edit_task.html",
        {
            "task": task
        }
    )


def delete_task(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id
    )

    if request.method == "POST":

        task.delete()

    return redirect("task_list")


def toggle_star(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id
    )

    task.starred = not task.starred

    task.save()

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "task_list"
        )
    )


def toggle_complete(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id
    )

    task.completed = not task.completed

    task.save()

    return redirect(
        request.META.get(
            "HTTP_REFERER",
            "task_list"
        )
    )