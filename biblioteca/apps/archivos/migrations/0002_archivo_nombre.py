# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivo',
            name='nombre',
            field=models.CharField(default='Hola', max_length=30),
            preserve_default=False,
        ),
    ]
