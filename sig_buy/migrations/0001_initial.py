# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SigBuy',
            fields=[
                ('date', models.DateField(auto_created=True)),
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('code', models.CharField(default='00000000', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('code', models.CharField(default='00000000', max_length=20)),
                ('name', models.CharField(default='A\u80a1\u5927\u80a1\u7968', max_length=35)),
            ],
        ),
    ]
