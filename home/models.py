# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import time
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.dispatch import receiver
from django.http import request
from allauth.account.signals import user_signed_up


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follow=models.ManyToManyField(User,blank=True,related_name="follow",null=True)
    dob = models.DateField(blank=True,null=True)
    profpic=models.ImageField(upload_to='media/',blank=True)


    def __str__(self):
        return self.user.first_name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    if sociallogin:
        # import pdb
        # pdb.set_trace()
        b=user.id
        user.profile.follow.add(b)
        a=sociallogin.account.extra_data['birthday']
        b=time.strptime(a,"%m/%d/%Y")
        c=time.strftime("%Y-%m-%d",b)
        user.refresh_from_db()
        print user.first_name
        user.profile.dob=c
        user.profile.save()



