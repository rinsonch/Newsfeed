# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20171113_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='feedimage',
            field=models.ImageField(blank=True, upload_to='feedimages/'),
        ),
    ]
