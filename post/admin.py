from __future__ import unicode_literals
from django.contrib import admin
from post.models import NewsFeed
from  post.models import NewsValue

admin.site.register(NewsValue)
admin.site.register(NewsFeed)
