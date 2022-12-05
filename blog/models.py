from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='название авто')
    year = models.CharField(max_length=150, blank=True, null=True, verbose_name='Год выпуска')
    transmitter = models.CharField(max_length=150, blank=True, null=True, verbose_name='Коробка передач')
    fuel_type = models.CharField(max_length=150, blank=True, null=True, verbose_name='Вид топлива')
    phone = models.CharField(max_length=150, blank=True, null=True, verbose_name='Номер телефона')
    kilometers = models.CharField(max_length=150, blank=True, null=True, verbose_name='Пробег')
    color = models.CharField(max_length=150, blank=True, null=True, verbose_name='цвет')
    price = models.CharField(max_length=150, blank=True, null=True, verbose_name='цена')
    engine_capacity = models.CharField(max_length=150, blank=True, null=True, verbose_name='Объем двигателя')
    content = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo1 = models.ImageField(upload_to='photo1/', blank=True, null=True, verbose_name='Фото-1')
    photo2 = models.ImageField(upload_to='photo2/', blank=True, null=True, verbose_name='Фото-2')
    photo3 = models.ImageField(upload_to='photo3/', blank=True, null=True, verbose_name='Фото-3')
    photo4 = models.ImageField(upload_to='photo4/', blank=True, null=True, verbose_name='Фото-4')
    photo5 = models.ImageField(upload_to='photo5/', blank=True, null=True, verbose_name='Фото-5')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано ли')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автор')

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']






