# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swaps', '0002_auto_20150204_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'apps/swaps/media/photos', blank=True),
            preserve_default=True,
        ),
    ]
