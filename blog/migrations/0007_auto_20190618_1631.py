# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-18 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190611_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='姓名'),
        ),
    ]