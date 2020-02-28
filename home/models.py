# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class LeftMenu(models.Model):
    menuName = models.CharField(max_length=30)

class SitePost(models.Model):
    postTitle = models.CharField(max_length=30)
    postName = models.TextField()
    postText = models.TextField()
    postUrl = models.CharField(max_length=30)
    LastUpdated = models.DateField()
    leftMenu = models.ForeignKey(LeftMenu, on_delete=models.CASCADE)

    def __str__(self):
        return postTitle
