# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-22 15:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('sender_customer_number', models.CharField(blank=True, max_length=20)),
                ('sender_telephone_number', models.CharField(max_length=15)),
                ('sender_email', models.EmailField(blank=True, max_length=254)),
                ('sender_country', models.CharField(max_length=200)),
                ('sender_street_name', models.CharField(max_length=200)),
                ('sender_street_number', models.PositiveSmallIntegerField()),
                ('sender_postal_code', models.CharField(max_length=16)),
                ('recipient_customer_number', models.CharField(blank=True, max_length=20)),
                ('recipient_telephone_number', models.CharField(max_length=15)),
                ('recipient_email', models.EmailField(blank=True, max_length=254)),
                ('recipient_country', models.CharField(max_length=200)),
                ('recipient_street_name', models.CharField(max_length=200)),
                ('recipient_street_number', models.PositiveSmallIntegerField()),
                ('recipient_postal_code', models.CharField(max_length=16)),
                ('package_height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('package_width', models.DecimalField(decimal_places=2, max_digits=5)),
                ('package_length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('package_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('collect_on_delivery', models.BooleanField(default=False)),
                ('collect_on_delivery_amount', models.IntegerField(blank=True, default=0)),
                ('is_package_delivered', models.BooleanField(default=False)),
                ('additional_info', models.TextField(blank=True)),
                ('deliver_till', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
    ]
