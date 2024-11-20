from django.contrib import admin
from .models import Book  # Імпортуємо модель Book

# Реєструємо модель для відображення в адмін-панелі
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_year', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('genre', 'publication_year')
