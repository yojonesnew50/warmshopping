# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150715_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=b'products/image/1397823008_20.png', upload_to=b'products/image/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'products/image/1397823008_20.png', upload_to=b'products/image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='download',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/mike/Desktop/market-master/static/protected'), null=True, upload_to=products.models.download_loc),
        ),
    ]
