# -*- coding: utf-8 -*-
from django.db import models
from . import managers

# TODO - add some kind of tag system and a way to sort the gallery by tag

class ImageEntry(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    slug = models.SlugField(max_length=200, unique=True)
    caption = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    objects = managers.ImageEntryManager()

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ["-uploaded"]

    def __str__(self):
        return self.title
