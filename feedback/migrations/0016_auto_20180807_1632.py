# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-08-07 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.translation


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0015_feedback_max_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='language',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='language',
            field=models.CharField(default=django.utils.translation.get_language, max_length=255, null=True),
        ),
    ]
