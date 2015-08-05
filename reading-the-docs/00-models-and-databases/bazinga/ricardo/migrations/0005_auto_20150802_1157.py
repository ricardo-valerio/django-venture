# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ricardo', '0004_auto_20150802_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(verbose_name='album of the artist', to='ricardo.Musician'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='final_college_grade',
            field=models.IntegerField(verbose_name='musician final college grade'),
        ),
    ]
