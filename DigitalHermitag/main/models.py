from django.db import models
from django.contrib.auth.models import User


class Art(models.Model):
    title = models.CharField('Название картины', max_length=50)
    image_file = models.ImageField('Картина', upload_to='uploaded_images/')
    describition = models.CharField('Описание', max_length=250)
    author = models.CharField('Имя профиля', max_length=250, default='аноним')
    genre = models.CharField('Жанр', max_length=50, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картины'
