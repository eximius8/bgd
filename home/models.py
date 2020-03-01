# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class NewsItem(models.Model):
    newsName = models.CharField(max_length=100)
    newsText = models.TextField()
    datePublished = models.DateField()


class LeftMenu(models.Model):
    menuName = models.CharField(max_length=30)
    menuUrl = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.menuName

    def leftMenuDict(self,Flag=False):
        Lposts = self.sitepost_set.all().order_by('postUrl')
        Leftm = {}
        prefix="/"
        if Flag:
            prefix=""
        for pitem in Lposts:
            link=pitem.postUrl
            name=pitem.leftMenuName
            if link:
                Leftm[name]=prefix+self.menuUrl+'/'+link+'/'
            else:
                Leftm[name]=prefix+self.menuUrl+'/'
        return Leftm



class SitePost(models.Model):
    postTitle = models.CharField(max_length=40)
    leftMenuName = models.CharField(max_length=30)
    postText = models.TextField()
    postUrl = models.CharField(max_length=30, blank=True)
    LastUpdated = models.DateField()
    leftMenuName = models.CharField(max_length=30)
    leftMenu = models.ForeignKey(LeftMenu, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        if self.postUrl:
            return self.postTitle
        elif self.leftMenu:
            return "Дефолт для меню - " + self.leftMenu.menuName + ": " + self.postTitle
        else:
            return "Дефолт для начальной страницы: " + self.postTitle
