# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20161013_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='myrecord',
            name='edit_dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myrecord',
            name='edited_by',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]