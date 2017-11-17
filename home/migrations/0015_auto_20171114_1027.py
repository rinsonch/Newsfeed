# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20171114_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profpic',
            field=models.ImageField(blank=True, upload_to='profpics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
