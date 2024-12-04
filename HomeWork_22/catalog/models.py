from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=150, verbose_name='Наименование'),
    description = models.CharField(max_length=150, verbose_name='Описание')
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=150, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'



class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']
