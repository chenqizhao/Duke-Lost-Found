# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditem',
            name='found_category',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='founditem',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='lostitem',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='lostitem',
            name='lost_category',
            field=models.IntegerField(default=0),
        ),
    ]
