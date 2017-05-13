import models
from datetime import datetime

from datetime import  timedelta

class Delta:
	pass

class Day:
	d = None

	def __init__(self):
		self.d = datetime.date()


	def __add__(self, other):
		delta = timedelta(other)
		self.d = self.d + delta


	def __sub__(self, other):
		pass



class Stock:
	s = None  # models.Stock

	def __init__(self, stock):
		self.s = stock

	def save(self):
		s.save()

	def price(self, date):
		pass


class SigBuy:
	sb = None  # models.SigBuy

	def __init__(self, sigbuy):
		self.sb = sigbuy

	def __getattr__(self, attr):
		if attr == 'date':
			return self.sb.date

		if attr == 'code':
			# assert isinstance(self.sb.code, str)
			return self.sb.code


class Price:
	p = None  # models.Pirce

	def __init__(self, price):
		self.p = price

	def next(self):
		pass

	def __hasNext(self):
		pass

	def __getattr__(self, attr):
		if attr == 'date':
			return self.p.date

		if attr == 'stock':
			# assert isinstance(self.sb.code, str)
			# return self.p.st
			pass
