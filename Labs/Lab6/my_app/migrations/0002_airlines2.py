# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airlines2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('flight_id', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]