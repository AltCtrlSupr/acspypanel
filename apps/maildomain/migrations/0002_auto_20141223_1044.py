# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maildomain', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maildomain',
            name='description',
        ),
        migrations.AlterField(
            model_name='maildomain',
            name='max_aliases',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maildomain',
            name='max_mailboxes',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='maildomain',
            name='max_quota',
            field=models.BigIntegerField(default=10),
            preserve_default=True,
        ),
    ]
