# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yo_hack_app', '0004_auto_20141123_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='word1',
            field=models.CharField(default=b'dinner', max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
