# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class aboutpost(models.Model):
    postTitle = models.CharField(max_length=30)
    postName = models.TextField()
    postText = models.TextField()
    postUrl = models.CharField(max_length=30)
