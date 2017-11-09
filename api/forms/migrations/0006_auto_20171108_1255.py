# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_question_reversed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='max',
        ),
        migrations.RemoveField(
            model_name='question',
            name='min',
        ),
        migrations.AddField(
            model_name='form',
            name='max',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='min',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]