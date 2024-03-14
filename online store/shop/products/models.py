from django.db import models


# категории продуктов
class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Категории')
    description = models.TextField(blank=True, verbose_name='Описание категорий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = "Категории"


# ТОВАРЫ
class Products(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название товара')  # название товара
    image = models.ImageField(upload_to='products_images/', blank=True, verbose_name='Изображение')  # 1 картинка товара
    description = models.TextField(blank=True, verbose_name='Описание')
    short_description = models.CharField(max_length=100, blank=True, verbose_name='Краткое описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена')
