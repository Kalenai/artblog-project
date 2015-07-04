from django.contrib import admin
from . import models

@admin.register(models.ImageEntry)
class ImageEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title"]
