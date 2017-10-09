# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 11:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dgi', '0010_auto_20170314_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='detail_reference',
            field=models.CharField(default='', max_length=50, verbose_name='D\xe9tail R\xe9f\xe9rence'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date_post',
            field=models.DateField(default=datetime.datetime(2017, 3, 14, 11, 45, 37, 312000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='publication',
            name='libelle_reference',
            field=models.CharField(default='', max_length=50, verbose_name='Libelle R\xe9f\xe9rence'),
        ),
    ]
