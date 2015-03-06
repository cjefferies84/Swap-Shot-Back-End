# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swaps', '0003_auto_20150211_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swap',
            name='name',
        ),
    ]
