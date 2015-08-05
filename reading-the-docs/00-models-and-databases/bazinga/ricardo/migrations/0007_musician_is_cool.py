# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ricardo', '0006_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='is_cool',
            field=models.BooleanField(default=True),
        ),
    ]
