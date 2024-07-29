from django.db import models

class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Модель')
    price = models.FloatField(verbose_name='Цена')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    
    def __str__(self):
        return self.title
