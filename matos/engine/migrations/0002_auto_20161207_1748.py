# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operation',
            options={'ordering': ('date',)},
        ),
        migrations.AddField(
            model_name='operation',
            name='result',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
