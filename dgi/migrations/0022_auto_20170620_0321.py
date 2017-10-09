# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 03:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dgi', '0021_auto_20170620_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratoire',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 20, 3, 21, 46, 466000, tzinfo=utc), verbose_name='Date de Publication'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date_post',
            field=models.DateField(default=datetime.datetime(2017, 6, 20, 3, 21, 46, 467000, tzinfo=utc)),
        ),
    ]