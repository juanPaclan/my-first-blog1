# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
