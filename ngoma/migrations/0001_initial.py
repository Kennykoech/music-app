# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('song_logo', models.FileField(upload_to='')),
                ('song_title', models.CharField(max_length=100)),
                ('song', models.FileField(upload_to='')),
            ],
        ),
    ]
