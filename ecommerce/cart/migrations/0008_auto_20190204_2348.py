# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-04 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20190203_1839'),
        ('cart', '0007_auto_20190204_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
