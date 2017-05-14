# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sig_buy', '0003_auto_20170513_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='code',
            field=models.CharField(default='00000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='sigbuy',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 14, 15, 28, 40, 285732), auto_created=True),
        ),
    ]
