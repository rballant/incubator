# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-09-29 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20151220_2237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('start', 'stop'), 'verbose_name': 'Événement'},
        ),
    ]