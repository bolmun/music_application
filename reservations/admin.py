from django.contrib import admin
from . import models


@admin.register(models.Reservtion)
class ReservatioAdmin(admin.ModelAdmin):

    list_display = (
        "status",
        "student",
        "resume",
        "meeting_time",
        "meeting_address",
    )

    search_fields = ("student__username",)

    ordering = ("status",)
