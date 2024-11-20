from django.db import models # Для создания моделей базы данных.

class Book(models.Model):
    '''Описывает модель таблицы БД.'''

    title = models.CharField(max_length=255) # Колонка = названию книг в таблице БД (строка)
    author = models.CharField(max_length=255) # Колонка = имя автора в таблице БД (строка)
    genre = models.CharField(max_length=100) # Колонка = жанр книги в таблице БД (строка)
    publication_year = models.PositiveIntegerField() # Колонка = год публикации в таблице БД (положительные числа)
    created_at = models.DateTimeField(auto_now_add=True) # Колонка = дата и время создания записи

    def __str__(self):
        return self.title

