# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendor_daily_pl_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_daily_pl',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]