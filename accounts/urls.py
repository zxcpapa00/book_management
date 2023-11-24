from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegistrationUserAPIView

urlpatterns = [
    path('register/', RegistrationUserAPIView.as_view()),  # Регистрация пользователя
    path('auth-drf/', include('rest_framework.urls')),  # auth-drf/login - логинимся, auth-drf/logout - разлогиниваемся
    path('auth/token', obtain_auth_token, name='token'),
]
