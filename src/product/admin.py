from django.contrib import admin
from product.models import Product


# register models for admin dashboard
admin.site.register(Product)
