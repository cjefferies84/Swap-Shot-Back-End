# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swaps', '0002_auto_20150210_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.CharField(max_length=15, choices=[(b'Poor', b'Poor'), (b'Fair', b'Fair'), (b'Good', b'Good'), (b'Excellent', b'Excellent'), (b'Like New', b'Like New'), (b'New', b'New')]),
            preserve_default=True,
        ),
    ]
