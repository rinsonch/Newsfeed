# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import NewsFeed
from  models import NewsValue

admin.site.register(NewsValue)
admin.site.register(NewsFeed)
