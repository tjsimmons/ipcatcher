# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20170128_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='ip',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='last_check_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
