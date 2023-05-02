from django.db import models

# Create your models here.

"""
class TipeOfProductModel(models.Model):
    
    name = models.TextField(verbose_name="Nombre", max_length=50, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Tipo de productos"
        verbose_name_plural = "Tipos de productos"

        

class CategoryModel(models.Model):
    
    name = models.TextField(verbose_name="Nombre", max_length=50, unique=True, null=False, blank=False)

    tipe_of_product = models.CharField(verbose_name="Tipe of product", max_length=50, unique=True, null=False, blank=False,)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
"""


class ProductModel(models.Model):

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def url_generator(self, file_name:str) -> str:
        return f"products/img/{file_name}"


    name = models.CharField(verbose_name="Nombre", max_length=50, unique=True, null=False, blank=False)

    price = models.DecimalField(verbose_name="Precio", max_digits=9, decimal_places=2,  null=False, blank=False)
    
    description = models.TextField(verbose_name="descripcion", max_length=50, unique=True, null=False, blank=False)

    img = models.ImageField(verbose_name="Imagen", upload_to=url_generator)

    stock = models.BooleanField(verbose_name="Stock")
        