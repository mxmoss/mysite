# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-07 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20161028_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myrecord',
            name='birth_dt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='myrecord',
            name='comments_txt',
            field=models.TextField(blank=True, default=''),
        ),
    ]
