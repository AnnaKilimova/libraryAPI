from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password')
        self.admin = User.objects.create_superuser(username='admin', password='password')
        self.book = Book.objects.create(title="Test Book", author="Test Author", genre="Fiction", publication_year=2020)

    def test_get_books(self):
        self.client.login(username='user', password='password')
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        self.client.login(username='user', password='password')
        data = {"title": "New Book", "author": "New Author", "genre": "Non-fiction", "publication_year": 2023}
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_book_as_admin(self):
        self.client.login(username='admin', password='password')
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book_as_user(self):
        self.client.login(username='user', password='password')
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
