# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='img_index',
            new_name='img',
        ),
        migrations.AlterField(
            model_name='company',
            name='intro',
            field=models.TextField(default='', max_length=2048),
        ),
    ]
