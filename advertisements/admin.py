from django.contrib import admin
from . import models


@admin.register(
    models.LessonType, models.PreferStyle, models.instrumentChoice, models.LessonDay,
)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):

    pass
