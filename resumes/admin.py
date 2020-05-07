from django.contrib import admin
from . import models


@admin.register(models.instrumentChoice)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
