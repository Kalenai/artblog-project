from django.contrib import admin
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "published")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "tags"]

admin.site.register(models.Tag)
