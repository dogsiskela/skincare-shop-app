from django.contrib import admin

from product.models import Product,ProductTag

admin.site.register(ProductTag)
admin.site.register(Product)
