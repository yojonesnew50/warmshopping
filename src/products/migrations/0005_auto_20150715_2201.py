# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150708_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured',
            name='products',
            field=models.ManyToManyField(to='products.Product', blank=True),
        ),
    ]
