# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0002_auto_20160102_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='moderated',
            field=models.BooleanField(default=False),
        ),
    ]