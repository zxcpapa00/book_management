from rest_framework import generics
from rest_framework.permissions import AllowAny

from book.models import Book
from book.serializers import BookSerializer


class BookListAPIView(generics.ListAPIView):
    """Список всех книг"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailAPIView(generics.RetrieveAPIView):
    """Информация о конкретной книге"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookCreateAPIVIew(generics.CreateAPIView):
    """Создание книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookUpdateAPIView(generics.RetrieveUpdateAPIView):
    """Обновление данных о книге"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDeleteAPIView(generics.RetrieveDestroyAPIView):
    """Удаление книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
