from django.db import models


class Task(models.Model):

    CATEGORY_CHOICES = [
        ("Self", "Self"),
        ("Work", "Work"),
        ("Study", "Study"),
        ("Personal", "Personal"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="Other"
    )

    completed = models.BooleanField(default=False)

    starred = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title