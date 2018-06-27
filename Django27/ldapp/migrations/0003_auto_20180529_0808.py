# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-29 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ldapp', '0002_auto_20180529_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField()),
                ('hcontent', models.CharField(max_length=100)),
                ('hBook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldapp.BookInfo')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]
