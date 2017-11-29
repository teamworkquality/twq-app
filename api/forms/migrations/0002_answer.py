# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 00:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20171119_1938'),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.Employee')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Form')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Question')),
            ],
        ),
    ]
