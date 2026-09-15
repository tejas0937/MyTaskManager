from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "completed",
        "starred",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "category",
        "completed",
        "starred",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "-created_at",
    )