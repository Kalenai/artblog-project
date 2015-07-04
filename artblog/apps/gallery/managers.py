# -*- coding: utf-8 -*-
from django.db import models

class ImageEntryManager(models.Manager):
    def visible(self):
        return self.filter(visible=True)
