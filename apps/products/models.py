from django.db import models

# Create your models here.
     
class CategoryModel(models.Model):
    
    name = models.CharField(
        verbose_name="Nombre", max_length=100, unique=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        
        ordering = ['name']

class ProductModel(models.Model):

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

        ordering = ['category', '-stock']

    def url_generator(self, file_name:str) -> str:
        return f"products/img/{file_name}"


    name = models.CharField(verbose_name="Nombre", max_length=50, unique=True, null=False, blank=False)

    price = models.DecimalField(verbose_name="Precio", max_digits=9, decimal_places=2,  null=False, blank=False)
    
    category = models.ForeignKey(CategoryModel, verbose_name="Categoria", on_delete=models.PROTECT, null=False, blank=False, to_field='name' )
    
    description = models.TextField(verbose_name="descripcion", max_length=50, null=True, blank=True)

    img = models.ImageField(verbose_name="Imagen", upload_to=url_generator, null=True, blank=True)

    stock = models.BooleanField(verbose_name="Stock")
        