from django.db import models

class ProductTag(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='src/media/products/', default = 'src/media/products/default.png')
    description = models.CharField(max_length=1000)
    price = models.FloatField() 
    category = models.ManyToManyField(ProductTag)
    in_stock = models.IntegerField()
    
    def __str__(self):
        return self.name
    