# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-06 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('division', models.IntegerField(default=1)),
                ('locate', models.CharField(max_length=30)),
                ('day', models.CharField(max_length=1)),
                ('time', models.CharField(max_length=30)),
                ('prof', models.CharField(max_length=15)),
            ],
        ),
    ]
