# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_images_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='thumbnail',
            field=models.CharField(default='old', max_length=256),
            preserve_default=False,
        ),
    ]
