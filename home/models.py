# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class LeftMenu(models.Model):
    menuName = models.CharField(max_length=30)
    #menuUrl = models.OneToOneField

    def __str__(self):
        return self.menuName

    def MenuUrl(self):
        return SitePost.objects.filter(leftMenu==self).first().postUrl


class SitePost(models.Model):
    postTitle = models.CharField(max_length=40)
    leftMenuName = models.CharField(max_length=30)
    postName = models.TextField()
    postText = models.TextField()
    postUrl = models.CharField(max_length=30)
    LastUpdated = models.DateField()
    leftMenuName = models.CharField(max_length=30)
    leftMenu = models.ForeignKey(LeftMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.postTitle
