#!/usr/bin/python
# coding=utf-8
from django.core.management.base import BaseCommand
from optparse import make_option
# from django.core.exceptions import Do
import tushare as ts
from sig_buy.models import Stock


def init_stock_names():
	print "init_stock_names"
	basics = ts.get_stock_basics()
	names = basics['name']

	cnt = 0
	for i in names.index:
		try:
			s = Stock.objects.get(code=i)
			if s.name == names[i]:
				pass
			else:
				#print u"rename %s %s -> %s" % (str(s.code), str(s.name), str(names[i]))
				print s.name
				print names[i]
				s.name = names[i]
				s.save()
				print "rename :%s"%s.code
		except Stock.DoesNotExist,e:
			print e
			s=Stock(code=i,name=names[i])
			s.save()

		finally:
			cnt += 1

	print "Total %d stock" % cnt


def get_name_by_code(code):
	global stock_names

	if stock_names is None:
		print "stock_names is None!"
		init_stock_names()

	return stock_names[code]


if __name__ == "__main__":
	print get_name_by_code("600606")


class Command(BaseCommand):
	option_list = BaseCommand.option_list + ( \
		make_option('-o', '--obsolete', dest="obsolete", action='store_true', help=u'to show obsolete signal buy'), \
		make_option('-d', '--date', dest="date", default=20170510, action='store', type='int', help=u'日期'), \
		make_option('-l', '--list', dest="list", default=False, action='store', type='string', help=u'信号列表'), \
		make_option('-c', '--code', dest="code", default=0, action='store', type='int', help=u'股票代码'), \
		make_option('-a', '--add', dest="add", action='store', type='string', help=u'增加股票代码'), \
		make_option('-b', '--buy', dest="buy", default=False, type='string', help=u'执行买入操作'), \
		)

	def handle(self, *args, **options):
		init_stock_names()
