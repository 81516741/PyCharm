# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(default='', max_length=20)),
                ('paddress', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
