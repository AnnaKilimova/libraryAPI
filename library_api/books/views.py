from rest_framework.viewsets import ModelViewSet # CRUD-операции для модели.
from rest_framework.permissions import IsAuthenticated, IsAdminUser # Проверка прав доступа.
from rest_framework.filters import SearchFilter # Добавляет функциональность поиска в API.
from django_filters.rest_framework import DjangoFilterBackend # Фильтрация данные по указанным полям модели.

from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    '''Представление для работы с моделью Book.'''

    queryset = Book.objects.all() # Определяет, какие поля модели будут использоваться в представлении: все.
    serializer_class = BookSerializer # Указывает, какой сериализатор использовать для модели.
    authentication_classes = []  # Token Authentication is used globally
    permission_classes = [IsAuthenticated] # Список классов для проверки прав доступа: только аутентифицированные пользователи.
    filter_backends = [DjangoFilterBackend, SearchFilter] # Классы для фильтрации и поиска данных.
    filterset_fields = ['author', 'genre', 'publication_year'] # Поля модели, по которым можно фильтровать данные.
    search_fields = ['title'] # Задает поля модели, по которым можно выполнять поиск.

    def get_permissions(self):
        '''Переопределяет базовый метод get_permissions DRF.
           Здесь настраиваются динамические разрешения.'''

        if self.action == 'destroy': # Определяет, выполняется ли удаление.
            self.permission_classes = [IsAdminUser] # Разрешение обновляется для проверки, что пользователь является администратором.
        return super().get_permissions()
