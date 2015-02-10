# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.CharField(max_length=15, choices=[(b'POOR', b'Poor'), (b'FAIR', b'Fair'), (b'GOOD', b'Good'), (b'EXCELLENT', b'Excellent'), (b'LIKE_NEW', b'Like New'), (b'NEW', b'New')]),
            preserve_default=True,
        ),
    ]
