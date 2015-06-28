# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django_markdown.models import MarkdownField
from . import managers

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug


# TODO - fix this so that images are responsive.  likely means switching from markdown to an HTML editor like CKEditor
class Post(models.Model):
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)

    title = models.CharField(max_length=200)
    body = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = managers.PostManager()

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-created"]

    def __str__(self):
        return self.title
