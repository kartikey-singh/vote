# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-15 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
