# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='download',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/jmitch/Dropbox/cfeprojects/static/protected'), null=True, upload_to=products.models.download_loc),
        ),
    ]
