# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swap',
            name='status',
            field=models.CharField(default=b'AVAILABLE', max_length=15, choices=[(b'AVAILABLE', b'Available'), (b'CLOSED', b'Closed'), (b'PENDING', b'Pending')]),
            preserve_default=True,
        ),
    ]
