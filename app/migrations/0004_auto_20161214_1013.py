# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_images_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='thumbnail',
            field=models.FileField(upload_to=''),
        ),
    ]
