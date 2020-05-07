from django.contrib import admin
from . import models


@admin.register(models.instrumentChoice)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("resume_title", "instructor", "instrument", "city", "fee")},
        ),
        (
            "Education",
            {"fields": ("final_degree", "college", "is_graduated", "graduate_year")},
        ),
        ("Performance", {"fields": ("awards", "career", "youtube_link")},),
        ("More", {"fields": ("is_super_instructor",)},),
    )

    list_display = (
        "instructor",
        "instrument",
        "final_degree",
        "college",
        "city",
        "fee",
        "is_super_instructor",
    )

    list_filter = ("city", "instrument", "is_super_instructor")

    search_fields = ("=city", "^instructor__username")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
