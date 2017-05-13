from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import SigBuy,Stock


class StockAdmin(admin.ModelAdmin):
    list_display = ('seq', 'code','name')
    search_fields =('code', 'name')

admin.site.register(Stock, StockAdmin)