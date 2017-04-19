# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 05:46
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restimage',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='app/restimage/%Y/%m/%d'),
        ),
    ]
