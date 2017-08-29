# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-29 14:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0002_auto_20170817_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='user',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='from_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u53d1\u9001\u6d88\u606f\u7684\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='to_user',
            field=models.IntegerField(default=0, verbose_name='\u6536\u6d88\u606f\u7684\u7528\u6237'),
        ),
    ]
