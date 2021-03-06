# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 17:27
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=30)),
                ('numbers', django.contrib.postgres.fields.jsonb.JSONField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
    ]
