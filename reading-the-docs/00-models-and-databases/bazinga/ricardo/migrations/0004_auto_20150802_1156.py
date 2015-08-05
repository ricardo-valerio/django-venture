# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ricardo', '0003_musician_shirt_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='final_college_grade',
            field=models.IntegerField(verbose_name='Musician final college grade', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='ricardo.Musician', verbose_name='Album of the artist'),
        ),
    ]
