# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-30 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')], max_length=3)),
                ('birth_day', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('authors', models.ManyToManyField(to='books.Author2')),
            ],
        ),
    ]