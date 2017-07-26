# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 14:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_crm', '0003_auto_20170724_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]