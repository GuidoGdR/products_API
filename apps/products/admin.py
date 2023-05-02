from django.contrib import admin

from .models import ProductModel

# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    list_display = ("name", "price", "stock")
    search_fields = ("name",)
    list_filter = ("stock",)
    

admin.site.register(ProductModel, ProductAdmin)
