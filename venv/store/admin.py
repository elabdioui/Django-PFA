from django.contrib import admin
from .models import Product,CustomUser,Cart

# Register your models here.

admin.site.register(Product)
admin.site.register(CustomUser)
admin.site.register(Cart)
