from django.contrib import admin
from orders.models import Category, Product, Orders

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Orders)
