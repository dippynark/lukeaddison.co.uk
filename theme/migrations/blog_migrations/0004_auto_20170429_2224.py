# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='subtitle',
            field=models.CharField(blank=True, help_text='The subtitle over the background', max_length=200, null=True, verbose_name='Subtitle'),
        ),
    ]