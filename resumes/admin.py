from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.instrumentChoice)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("title", "used_by")

    def used_by(self, obj):
        return obj.resumes.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

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
        "count_photos",
        "total_rating",
    )

    raw_id_fields = ("instructor",)

    list_filter = ("city", "instrument", "is_super_instructor")

    search_fields = ("=city", "^instructor__username")

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50px' src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"
