# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(default='python', max_length=100),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='style',
            field=models.CharField(default='friendly', max_length=100),
        ),
    ]
