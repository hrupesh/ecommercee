# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-05 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dp', '0003_auto_20190204_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='dp_order_model',
            name='status_order',
            field=models.CharField(choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], default='started', max_length=120),
        ),
    ]
