# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 01:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dgi', '0017_auto_20170619_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=8)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dgi.Formation')),
            ],
        ),
        migrations.CreateModel(
            name='TypeInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='serviceedgi',
            options={'verbose_name': 'Service E-DGI'},
        ),
        migrations.AlterField(
            model_name='information',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 20, 1, 19, 58, 458000, tzinfo=utc), verbose_name='Date de Publication'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date_post',
            field=models.DateField(default=datetime.datetime(2017, 6, 20, 1, 19, 58, 458000, tzinfo=utc)),
        ),
    ]
