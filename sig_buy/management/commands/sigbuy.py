#!/usr/bin/python
#coding=utf-8
from django.core.management.base import BaseCommand
from optparse import make_option

class Command(BaseCommand):
	option_list = BaseCommand.option_list+(\
		make_option('-o','--obsolete',dest="obsolete",action='store_true',help=u'to show obsolete signal buy'),\
		make_option('-d','--date',dest="date",default=20170510,action='store',type='int',help=u'日期'),\
		make_option('-l','--list',dest="list",default=False,action='store',type='string',help=u'信号列表'),\
		make_option('-c','--code',dest="code",default=0,action='store',type='int',help=u'股票代码'),\
		make_option('-a','--add',dest="add",action='store',type='string',help=u'增加股票代码'),\
		)

	def handle(self, *args, **options):
		print "by %s"%str(options)

