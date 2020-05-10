from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservatioAdmin(admin.ModelAdmin):

    list_display = (
        "status",
        "student",
        "resume",
        "meeting_time",
        "meeting_address",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)

    search_fields = ("student__username",)

    ordering = ("status",)
