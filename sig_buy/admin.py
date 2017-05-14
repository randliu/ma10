
from django.contrib import admin
# Register your models here.
from django.contrib import admin
from models import SigBuy, Stock


class StockAdmin(admin.ModelAdmin):
	list_display = ('seq', 'code', 'name')
	search_fields = ('code', 'name')


admin.site.register(Stock, StockAdmin)


class SigBuymin(admin.ModelAdmin):
	list_display = ('seq', 'date', 'code', 'name')
	search_fields = ('code', 'date')

	def name(self, obj):
		stock = Stock.objects.get(code=obj.code)
		return stock.name

		#return u"BBB"


admin.site.register(SigBuy, SigBuymin)
