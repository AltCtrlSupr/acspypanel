# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingkey',
            name='type',
            field=models.CharField(default=b'string', max_length=10, choices=[(b'string', b'String'), (b'check', b'Check Box'), (b'int', b'Integer'), (b'model', b'Model')]),
            preserve_default=True,
        ),
    ]
