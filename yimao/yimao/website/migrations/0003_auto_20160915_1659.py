# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20160831_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_detail_arg',
            field=models.TextField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_detail_detail',
            field=models.TextField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_detail_index',
            field=models.TextField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_index',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
