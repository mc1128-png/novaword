# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-05 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0021_usertask_added_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningplan',
            name='finished_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='完成时间'),
        ),
    ]
