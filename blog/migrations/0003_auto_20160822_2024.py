# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-22 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160822_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='package_id',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=100, unique=True),
        ),
    ]