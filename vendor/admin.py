from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(ChartOfAccounts)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Coupon)
admin.site.register(Order)

admin.site.register(OrderItems)
admin.site.register(Attributes)