# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 11:07
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20170429_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='background',
            field=mezzanine.core.fields.FileField(max_length=2000, verbose_name='Background'),
        ),
    ]
