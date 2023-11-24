from django.urls import path
from .views import BookListAPIView, BookDetailAPIView, BookCreateAPIView, BookUpdateAPIView, BookDeleteAPIView

urlpatterns = [
    path('books-list/', BookListAPIView.as_view()),  # Список всех книг
    path('books-list/<int:pk>', BookDetailAPIView.as_view()),  # Определенная книга
    path('create-book/', BookCreateAPIView.as_view()),  # Создаем книгу
    path('books-list/<int:pk>/update/', BookUpdateAPIView.as_view()),  # Обновляем данные об определенной книге
    path('books-list/<int:pk>/delete/', BookDeleteAPIView.as_view()),  # Удаляем книгу по ее id
]
