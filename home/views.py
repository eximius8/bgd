# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from home.models import LeftMenu, SitePost
from django.shortcuts import render, HttpResponse


def hauptMenu():
    menus=LeftMenu.objects.all().exclude(menuUrl__exact='')
    menuT={}
    for Lmenu in menus:
        link=Lmenu.menuUrl
        name=Lmenu.menuName
        menuT[name]="/"+link
    return menuT


def SimplePost(request,lmenu='',postname=''):
    pageArray={}
    mainM=hauptMenu()
    pageArray['mainm']=mainM
    if lmenu:
        try:
            Lmenu = LeftMenu.objects.get(menuUrl=lmenu)
            pageArray['leftm']=Lmenu.leftMenuDict()
            if postname:
                PostObj=SitePost.objects.filter(postUrl=postname,leftMenu=Lmenu).first()
            else:
                PostObj=SitePost.objects.filter(postUrl='',leftMenu=Lmenu).first()
            pageArray['post_title']=PostObj.postTitle
            pageArray['page_content']=PostObj.postText
            pageArray['last_updated']=PostObj.LastUpdated
        except:
            try:
                Lmenu = LeftMenu.objects.get(menuUrl='')
                pageArray['leftm']=Lmenu.leftMenuDict(Flag=True)
                PostObj=SitePost.objects.filter(postUrl=lmenu).first()
                pageArray['post_title']=PostObj.postTitle
                pageArray['page_content']=PostObj.postText
                pageArray['last_updated']=PostObj.LastUpdated
            except:
                pageArray['leftm']={'vstu.ru': 'vstu.ru'}
                pageArray['post_title']="Что-то пошло не так"
                pageArray['page_content']="Что-то пошло не так, за Вами уже выехал воронок"
    else:
        Lmenu = LeftMenu.objects.get(menuUrl='')
        pageArray['leftm']=Lmenu.leftMenuDict(Flag=True)
        PostObj=SitePost.objects.filter(postUrl='',leftMenu=Lmenu).first()
        pageArray['post_title']=PostObj.postTitle
        pageArray['page_content']=PostObj.postText
        pageArray['last_updated']=PostObj.LastUpdated


    return render(request, 'home/base.html', pageArray)
