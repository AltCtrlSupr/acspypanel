# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('hosting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='content_type',
            field=models.ForeignKey(default=1, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='resource',
            unique_together=set([('name', 'content_type')]),
        ),
    ]
