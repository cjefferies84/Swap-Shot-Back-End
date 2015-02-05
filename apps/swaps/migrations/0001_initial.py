# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(null=True, upload_to=b'photos', blank=True)),
                ('description', models.TextField(max_length=250)),
                ('condition', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Swap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('initiator', models.ForeignKey(related_name='initiator_swap', to=settings.AUTH_USER_MODEL)),
                ('initiator_items', models.ManyToManyField(related_name='initiator_items_swap', to='swaps.Item')),
                ('other_party', models.ForeignKey(related_name='other_party_swap', to=settings.AUTH_USER_MODEL)),
                ('other_party_items', models.ManyToManyField(related_name='other_party_items_swap', to='swaps.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
