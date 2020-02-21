# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, HttpResponse

def SimplePost(request):

    return render(request, 'home/base.html',{})
