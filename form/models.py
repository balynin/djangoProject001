from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    customer_name = models.CharField(max_length=120, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электропочта')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Модель часов')
    details = models.TextField(verbose_name='Сообщение')
    happy = models.BooleanField(verbose_name='Вопрос решен?')
    date = models.DateField(auto_now_add=True, verbose_name='Время обращения')

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


