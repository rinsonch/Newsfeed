# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from home.models import Profile,User



class NewsFeed(models.Model):
    userid=models.ForeignKey(Profile,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    content=models.CharField(max_length=3000)
    pub_date=models.DateTimeField(auto_now_add=True)
    feedpic=models.ImageField(upload_to='media/feedimages/',blank=True,null=True)
    like = models.ManyToManyField(User,blank=True,null=True,related_name='like')
    dislike = models.ManyToManyField(User,blank=True,null=True,related_name='dislike')

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.userid.user.first_name+" "+self.title


class NewsValue(models.Model):
    feedname=models.ForeignKey(NewsFeed,on_delete=models.CASCADE)
    commented=models.ForeignKey(Profile,on_delete=models.CASCADE)
    comment=models.CharField(max_length=150)
    comm_date=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-comm_date']

    def __str__(self):
        return self.comment




