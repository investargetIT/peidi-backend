from django.contrib import admin

# Register your models here.
from .models import orders, tradeOrders
admin.site.register(orders)
admin.site.register(tradeOrders)
