# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 10:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('dgi', '0008_auto_20170314_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='encadrements',
            field=tinymce.models.HTMLField(default='This is a text', null=True, verbose_name='Encadrements'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='enseignements',
            field=tinymce.models.HTMLField(default='This is a text', null=True, verbose_name='Enseignements'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='parcours_aca',
            field=tinymce.models.HTMLField(default='This is a text', null=True, verbose_name='Parcours Acad\xe9mique'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='parcours_pro',
            field=tinymce.models.HTMLField(default='This is a text', null=True, verbose_name='Parcours Professionnel'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='recherches',
            field=tinymce.models.HTMLField(default='This is a text', null=True, verbose_name='Recherches'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date_post',
            field=models.DateField(default=datetime.datetime(2017, 3, 14, 10, 22, 18, 512000, tzinfo=utc)),
        ),
    ]
