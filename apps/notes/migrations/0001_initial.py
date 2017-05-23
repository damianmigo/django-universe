# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 20:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('content_markdown', models.TextField()),
                ('content_html', models.TextField()),
                ('date_published', models.DateField(default=datetime.date.today)),
                ('slug', models.SlugField(max_length=255)),
                ('label', models.CharField(db_index=True, max_length=255)),
                ('icon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.Icon')),
            ],
        ),
    ]