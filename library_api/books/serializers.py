from rest_framework import serializers # Преобразует данные модели в формат JSON и обратно.
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    '''Преобразует данные модели в формат JSON и обратно.'''

    class Meta:
        '''Cообщает сериализатору, какую модель и какие поля использовать.'''

        model = Book # указывает модель БД, с которой будет работать сериализатор.
        fields = '__all__' # Определяет, какие поля модели должны быть включены в сериализатор: все.