# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-23 05:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=60)),
                ('aclass', models.CharField(max_length=16)),
                ('auptime', models.DateTimeField(default=datetime.datetime(2017, 3, 23, 5, 0, 8, 61132))),
                ('stars', models.IntegerField(default=0, max_length=10)),
                ('author', models.CharField(max_length=12)),
                ('apic', models.CharField(max_length=60)),
                ('acontect', models.TextField(max_length=10000)),
                ('amasonry', models.CharField(max_length=60)),
                ('watch', models.IntegerField(default=1437, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Qa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quser', models.CharField(max_length=12)),
                ('quesstion', models.CharField(max_length=64)),
                ('qtime', models.DateTimeField(default=datetime.datetime(2017, 3, 23, 5, 0, 8, 62211))),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Res',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resname', models.CharField(max_length=60)),
                ('http', models.CharField(max_length=128)),
                ('resclass', models.CharField(max_length=16)),
                ('uptime', models.DateTimeField(default=datetime.datetime(2017, 3, 23, 5, 0, 8, 59839))),
                ('price', models.IntegerField(max_length=5)),
                ('prow', models.IntegerField(max_length=10)),
                ('rpassword', models.CharField(max_length=6)),
                ('rpic', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=30)),
                ('qq', models.IntegerField(max_length=12)),
                ('regtime', models.DateTimeField(default=datetime.datetime(2017, 3, 23, 5, 0, 8, 58992))),
            ],
        ),
    ]