# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-22 16:32
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20160929_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, keep_meta=True, null=True, quality=0, size=[500, 500], upload_to='event_pictures'),
        ),
    ]
