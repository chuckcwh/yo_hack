# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('yo_hack_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.PositiveSmallIntegerField(choices=[(0, b'hello'), (1, b'help'), (2, b'location')])),
                ('text', models.TextField(null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ManyToManyField(related_name='actions_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='actions_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='profile',
            name='api_token',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
