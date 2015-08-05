# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ricardo', '0002_auto_20150802_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1, default='M'),
            preserve_default=False,
        ),
    ]
