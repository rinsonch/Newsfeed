# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 12:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_newsfeed_feedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsfeed',
            name='feedimage',
        ),
    ]
