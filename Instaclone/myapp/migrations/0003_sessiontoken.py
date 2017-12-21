# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20171221_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_token', models.CharField(max_length=255)),
                ('last_request_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to='myapp.UserModel')),
            ],
        ),
    ]
