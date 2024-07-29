from django.db import models

class Size(models.Model):
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    image = models.ImageField(null=True, upload_to='images')
    sizes = models.ManyToManyField(Size, verbose_name='объём', blank=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Модель')
    price = models.FloatField(verbose_name='Цена')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created = models.DateTimeField(null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения') 
    
    def __str__(self):
        return self.title

class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    text = models.TextField(verbose_name='текст отзыва')
    stars = models.IntegerField(
        choices=(
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5')
        )
        )
    author = models.CharField(max_length=100, null=True, verbose_name='автор', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.author