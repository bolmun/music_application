from django.contrib import admin
from . import models


@admin.register(models.Reservtion)
class ReservatioAdmin(admin.ModelAdmin):

    pass
