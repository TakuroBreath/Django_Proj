from django.db import models

NULLABLE = {'blank': 'True', 'null': 'True'}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    image = models.ImageField(verbose_name='Image', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Price')
    create_date = models.DateTimeField(verbose_name='Create Date')
    changed_date = models.DateTimeField(verbose_name='Changed')

    def __str__(self):
        return f'{self.category} - {self.name} - {self.price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
