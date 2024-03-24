from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'Category({self.name})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)
    created_at = models.DateField(verbose_name='Дата создания', **NULLABLE)
    updated_at = models.DateField(verbose_name='Дата изменения', **NULLABLE)

    def __str__(self):
        return f'Product({self.product_name})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    number_version = models.IntegerField(verbose_name="Номер версии")
    name = models.CharField(verbose_name="Название версии")
    is_active = models.BooleanField(default=False, verbose_name="Активная версия")

    def __str__(self):
        return f'{self.number_version}'

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
