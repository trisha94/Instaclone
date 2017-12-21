# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('has_verified_mobile', models.BooleanField(default=False)),
                ('created_On', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
