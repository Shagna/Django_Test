# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-07-15 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_delete_fixture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamA', models.CharField(max_length=50)),
                ('teamB', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('venues', models.CharField(max_length=50)),
                ('score', models.CharField(max_length=50)),
            ],
        ),
    ]
