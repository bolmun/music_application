from django.contrib import admin
from . import models


@admin.register(models.Report)
class ReportAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "instructor",
        "goal",
        "lesson_date",
        "achievement_score",
    )

    fieldsets = (
        ("Basic Info", {"fields": ("student", "instructor")},),
        ("Goal Setting", {"fields": ("goal", "due_date")},),
        ("Lesson Record", {"fields": ("lesson_date", "lesson_contents")},),
        (
            "Progress Report",
            {"fields": ("good_point", "bad_point", "achievement_score")},
        ),
        ("Homework", {"fields": ("homework",)},),
    )

    list_filter = ("instructor",)
    search_fields = ("^student__username", "^instructor__username")
