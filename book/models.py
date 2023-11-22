from django.db import models


class Book(models.Model):
    """Модель книги"""
    name = models.CharField('Название', max_length=512)
    author = models.CharField('Автор', max_length=256)
    year_publish = models.PositiveIntegerField('Год публикации')
    isbn = models.CharField('ISBN', max_length=256)

    def __str__(self):
        return self.name

