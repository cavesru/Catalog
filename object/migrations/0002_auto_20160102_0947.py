# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='moderated',
            field=models.BinaryField(),
        ),
    ]
