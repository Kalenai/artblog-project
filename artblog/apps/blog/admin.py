from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin

@admin.register(models.Post)
class PostAdmin(MarkdownModelAdmin):
    list_display = ("title", "created", "published")
    prepopulated_fields = {"slug": ("title",)}
    # TODO - add tags as a search field once they're implemented
    search_fields = ["title"]

admin.site.register(models.Tag)
