# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20150626_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='download',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/Mike/Desktop/market/static/protected'), null=True, upload_to=products.models.download_loc),
        ),
    ]
