# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_newsfeed_feedpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='content',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='newsfeed',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
