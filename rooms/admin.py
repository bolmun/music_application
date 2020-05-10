from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Amenity, models.Facility, models.Rule)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("title", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = (
        ("Basic Info", {"fields": ("name", "city", "address", "description")},),
        ("Price", {"fields": ("price_per_hour",)},),
        ("Spaces", {"fields": ("capacity", "amenities", "facilities", "rules")},),
        ("More Detail", {"fields": ("all_day", "instant_book", "host")},),
    )

    list_display = (
        "name",
        "city",
        "price_per_hour",
        "capacity",
        "all_day",
        "instant_book",
        "host",
    )

    raw_id_fields = ("host",)

    list_filter = (
        "amenities",
        "facilities",
        "rules",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
    )

    ordering = (
        "city",
        "capacity",
        "all_day",
        "price_per_hour",
    )

    search_fields = ("=city", "^host__username")

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width='50px' src='{obj.file.url}' />")

    get_thumbnail.short_description = "Thumbnail"
