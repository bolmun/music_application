from django.contrib import admin
from . import models


@admin.register(
    models.LessonType, models.PreferStyle, models.instrumentChoice, models.LessonDay,
)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("title", "used_by")

    def used_by(self, obj):
        return obj.ads.count()


@admin.register(models.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("student", "instrument", "category", "goal", "city")},
        ),
        ("Skill Info", {"fields": ("current_skill", "skill_reference")},),
        (
            "Lesson Requirement",
            {
                "fields": (
                    "min_fee",
                    "max_fee",
                    "lesson_count_per_week",
                    "desired_lesson_days",
                    "desired_lesson_time",
                    "desired_starting_date",
                    "lesson_type",
                    "prefer_style",
                )
            },
        ),
    )

    list_display = (
        "student",
        "instrument",
        "category",
        "city",
        "lesson_count_per_week",
        "min_fee",
        "max_fee",
        "desired_lesson_time",
        "count_style",
    )

    list_filter = (
        "category",
        "city",
        "lesson_count_per_week",
        "desired_lesson_days",
        "desired_lesson_time",
        "lesson_type",
        "prefer_style",
    )

    filter_horizontal = (
        "lesson_type",
        "prefer_style",
    )

    search_fields = ("=city", "^student__username")

    ordering = (
        "instrument",
        "category",
        "city",
        "lesson_count_per_week",
        "desired_lesson_time",
    )

    def count_style(self, obj):
        return obj.prefer_style.count()

    count_style.short_description = "선호 렛슨 스타일"
