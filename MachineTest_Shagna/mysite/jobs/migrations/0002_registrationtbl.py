# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-07-15 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrationtbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=50)),
                ('player1', models.CharField(max_length=50)),
                ('player2', models.CharField(max_length=50)),
                ('player3', models.CharField(max_length=50)),
                ('player4', models.CharField(max_length=50)),
                ('player5', models.CharField(max_length=50)),
                ('player6', models.CharField(max_length=50)),
                ('player7', models.CharField(max_length=50)),
                ('player8', models.CharField(max_length=50)),
                ('player9', models.CharField(max_length=50)),
                ('player10', models.CharField(max_length=50)),
                ('player11', models.CharField(max_length=50)),
                ('coach', models.CharField(max_length=50)),
                ('manager', models.CharField(max_length=50)),
            ],
        ),
    ]
