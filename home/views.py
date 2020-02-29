# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from home.models import LeftMenu, SitePost
from django.shortcuts import render, HttpResponse


def hauptMenu():
    menus=LeftMenu.objects.all()
    menuT={}
    for Lmenu in menus:
        #SitePost.objects.filter(leftMenu==Lmenu).first().postUrl
        link='/'+Lmenu.sitepost_set.first().postUrl
        name=Lmenu.menuName
        menuT[name]=link
    return menuT

def SimplePost(request):
    mainM=hauptMenu()

    return render(request, 'home/base.html',{'post_title': request.path, 'mainm': mainM})
