# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20171115_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profpic',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
