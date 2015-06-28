# -*- coding: utf-8 -*-
from django.db import models

class PostManager(models.Manager):
    def published(self):
        return self.filter(published=True)
