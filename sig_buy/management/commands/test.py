#!/usr/bin/python
#coding=utf-8
from django.core.management.base import BaseCommand
from optparse import make_option

class Command(BaseCommand):
	option_list = BaseCommand.option_list+(\
		make_option('-m','--market',dest="market",action='store',type='string',help='sh/sz/hk'),\
		make_option('-d','--day',dest="day",default=6,action='store',type='int',help='days'),\
		make_option('-i','--index',dest="index",default=False,action='store_true',help=u'各个市场的指数'),\
		make_option('-c','--code',dest="code",default=0,action='store',type='int',help=u'股票号码'),\
		)

	def handle(self, *args, **options):
		print "test %s"%str(options)

