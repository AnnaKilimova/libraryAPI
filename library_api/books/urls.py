from rest_framework.routers import DefaultRouter # Автоматически генерирует маршруты для ViewSet-ов.
from .views import BookViewSet

router = DefaultRouter() # Создание экземпляра класса для автоматической генерации маршрутов.
router.register(r'books', BookViewSet, basename='book') # Для регистрации ViewSet и его привязки к URL.

urlpatterns = router.urls # Список URL-шаблонов, сгенерированных маршрутизатором.
