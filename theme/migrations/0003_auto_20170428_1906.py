# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 18:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_remove_homepage_background'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='subheading',
        ),
    ]
