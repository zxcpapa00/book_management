## Тестовое задание для Python-разработчика

---
#### Инструкция по сборке Docker контейнеров:

1) Копируем репозиторий

- git clone https://github.com/zxcpapa00/book_management.git

2) Запускаем Docker Desktop
3) Собираем и запускаем образ

- docker-compose --env-file .env up -d --build 
--- 
#### Как пользоваться приложением
* 127.0.0.0:8000/api/v1/books/books-list/ - Получить список всех книг
* 127.0.0.0:8000/api/v1/books/books-list/int:pk - Информация об определенной книге 
* 127.0.0.0:8000/api/v1/books/create-book/ - Создать книгу 
* 127.0.0.0:8000/api/v1/books/books-list/int:pk/update/ - Обновить данные об определенной книге 
* 127.0.0.0:8000/api/v1/books/books-list/int:pk/delete/ - Удалить книгу по ее id
* 127.0.0.0:8000/api/v1/accounts/register/ - Зарегистрировать пользователя
* 127.0.0.0:8000/api/v1/accounts/auth-drf/login - Авторизовать пользователя