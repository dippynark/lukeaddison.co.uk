# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='subtitle',
            field=models.CharField(help_text='The subtitle over the background', max_length=200, null=True, verbose_name='Subtitle'),
        ),
    ]
