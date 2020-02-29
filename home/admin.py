# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from home.models import LeftMenu, SitePost

admin.site.register(SitePost)
admin.site.register(LeftMenu)

# Register your models here.
