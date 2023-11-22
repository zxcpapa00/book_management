from django.urls import path
from .views import BookListAPIView, BookDetailAPIView, BookCreateAPIVIew, BookUpdateAPIView, BookDeleteAPIView

urlpatterns = [
    path('books-list/', BookListAPIView.as_view()),
    path('books-list/<int:pk>', BookDetailAPIView.as_view()),
    path('create-book/', BookCreateAPIVIew.as_view()),
    path('books-list/<int:pk>/update/', BookUpdateAPIView.as_view()),
    path('books-list/<int:pk>/delete/', BookDeleteAPIView.as_view()),
]
