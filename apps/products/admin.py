from django.contrib import admin

from .models import ProductModel, CategoryModel

# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    list_display = ("name", "price", "category", "stock")
    search_fields = ("name",)
    list_filter = ("stock", "category")
    
admin.site.register(ProductModel, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name",)
    search_fields = ("name",)
    
admin.site.register(CategoryModel, CategoryAdmin)
