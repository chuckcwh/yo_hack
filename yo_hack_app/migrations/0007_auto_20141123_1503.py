# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yo_hack_app', '0006_auto_20141123_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='word2',
            field=models.CharField(default=b'I love you', max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
