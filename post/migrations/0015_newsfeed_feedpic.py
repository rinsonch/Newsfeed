# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_remove_newsfeed_feedpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='feedpic',
            field=models.ImageField(blank=True, null=True, upload_to='media/feedimages/'),
        ),
    ]
