from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField('Имя', max_length=128)
    email = models.EmailField('Электронная почта', unique=True)
    date_joined = models.DateTimeField('Дата регистрации', default=timezone.now)
    username = models.CharField(
        "Имя пользователя",
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            "unique": "Имя пользователя занято",
        },
    )

    REQUIRED_FIELDS = ["email", "first_name"]
