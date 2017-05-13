# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig_buy', '0002_auto_20170513_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ma10',
            old_name='price',
            new_name='value',
        ),
    ]
