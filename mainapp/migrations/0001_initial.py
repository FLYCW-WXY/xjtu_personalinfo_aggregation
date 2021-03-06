# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('time', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='borrowInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField()),
                ('title', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
    ]
