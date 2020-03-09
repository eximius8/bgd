# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from home.models import LeftMenu, SitePost, Equipment
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
import random as rnd


def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/') # or redirect('name-of-index-url')


def hauptMenu():
    menus=LeftMenu.objects.all().exclude(menuUrl__exact='')
    menuT={}
    for Lmenu in menus:
        link=Lmenu.menuUrl
        name=Lmenu.menuName
        menuT[name]="/"+link
    return menuT

def eqarray(simple=True):
    pageArray={}
    pageArray['rheader']="Наше оборудование"
    pageArray['ritems']={}
    allequip = Equipment.objects.all()
    act=rnd.randint(0,len(allequip)-1)
    counter=0
    for tool in allequip:
        if counter==act:
            pageArray['ritems'][tool.name]={'manufact': tool.manufact, 'urlimage': tool.urlimage, 'urlmenu': tool.postUrl, 'act': 'active'}
        else:
            pageArray['ritems'][tool.name]={'manufact': tool.manufact, 'urlimage': tool.urlimage, 'urlmenu': tool.postUrl, 'act': ''}
        counter=counter+1
    pageArray['simple']=simple
    return pageArray



def LabPost(request, toolu=''):
    pageArray={}
    mainM=hauptMenu()
    pageArray['mainm']=mainM
    Lmenu = LeftMenu.objects.get(menuUrl='lab')
    pageArray['leftm']=Lmenu.leftMenuEqDict()
    if not toolu:
        pageArray['simple']=True
        PostObj=SitePost.objects.filter(postUrl='',leftMenu=Lmenu).first()
        pageArray['post_title']=PostObj.postTitle
        pageArray['page_content']=PostObj.postText
        pageArray['last_updated']=PostObj.LastUpdated
    else:
        try:
            PostObj=Equipment.objects.filter(postUrl=toolu).first()
            pageArray['post_title']=PostObj.name
            pageArray['manufact'] = PostObj.manufact
            pageArray['urlimage'] = PostObj.urlimage
            pageArray['description'] = PostObj.description
            pageArray['longDescription'] = PostObj.longDescription
            pageArray['figureCaption'] = PostObj.figureCaption
            pageArray['last_updated']=PostObj.lastUpdated

        except:
            return HttpResponseRedirect('/lab/')


    pageArray2=eqarray(False)
    pageArray1={**pageArray2, **pageArray}


    return render(request, 'home/base.html', pageArray1)



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
                return HttpResponseRedirect('/')

    else:
        Lmenu = LeftMenu.objects.get(menuUrl='')
        pageArray['leftm']=Lmenu.leftMenuDict(Flag=True)
        PostObj=SitePost.objects.filter(postUrl='',leftMenu=Lmenu).first()
        pageArray['post_title']=PostObj.postTitle
        pageArray['page_content']=PostObj.postText
        pageArray['last_updated']=PostObj.LastUpdated

    pageArray2=eqarray()
    pageArray1={**pageArray2, **pageArray}

    return render(request, 'home/base.html', pageArray1)
