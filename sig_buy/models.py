# -*- coding: utf-8 -*-
#
from django.db import models


# Create your models here.


class Stock(models.Model):
    seq = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, default=u"00000000")
    name = models.CharField(max_length=35, default=u"A股大股票")


class SigBuyStatus:
    def __init__(self):
        pass

    VALID = u"VALID"  # 待处理
    OBSOLETE = u"OBSOLETE"  # 过期
    DONE = u"DONE"  # 已经执行


class SigBuy(models.Model):
    on = 'ON'
    off = 'off'
    buy = 'BUY'

    STATUS_CHOICES = (
        (on, 'On'),
        (off, 'Off'),
        (buy,'Buy'),
    )

    seq = models.AutoField(primary_key=True)
    date = models.DateField(auto_created=True)
    code = models.CharField(max_length=20, default=u"00000000")
    status = models.CharField(max_length=2,choices=STATUS_CHOICES,default=on)


class Price(models.Model):
    seq = models.AutoField(primary_key=True)
    date = models.DateField(auto_created=True)
    open = models.FloatField()
    close = models.FloatField()


class MA10(models.Model):
    seq = models.AutoField(primary_key=True)
    date = models.DateField(auto_created=True)
    value = models.FloatField()
    code = models.CharField(max_length=20, default=u"00000000")
