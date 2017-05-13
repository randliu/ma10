import tushare as ts
#from sig_buy.models import Stock
stock_names = None
def init_stock_names():
	global stock_names
	print "init_stock_names"
	basics=ts.get_stock_basics()
	names = basics['name']

	stock_names = names
	print names.tolist()
	for i in names.index:
		print i
		print names[i]


def get_name_by_code(code):
	global stock_names

	if stock_names is None:
		print "stock_names is None!"
		init_stock_names()

	return stock_names[code]


if __name__=="__main__":
	print get_name_by_code("600606")