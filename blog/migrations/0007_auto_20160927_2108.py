# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-27 19:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_packages_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='deliver_till',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
