# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig_buy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MA10',
            fields=[
                ('date', models.DateField(auto_created=True)),
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('price', models.FloatField()),
                ('code', models.CharField(default='00000000', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('date', models.DateField(auto_created=True)),
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='sigbuy',
            name='status',
            field=models.CharField(default=b'ON', max_length=2, choices=[(b'ON', b'On'), (b'off', b'Off'), (b'BUY', b'Buy')]),
        ),
    ]
