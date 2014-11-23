# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('yo_hack_app', '0002_auto_20141122_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('me', models.ForeignKey(related_name='families_me', to=settings.AUTH_USER_MODEL)),
                ('you', models.ForeignKey(related_name='families_you', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='profile',
            name='api_token',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
