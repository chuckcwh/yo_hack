# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yo_hack_app', '0005_auto_20141123_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='text',
            field=models.TextField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
