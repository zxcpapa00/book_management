from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegistrationUserAPIView

urlpatterns = [
    path('register/', RegistrationUserAPIView.as_view()),
    path('auth-drf/', include('rest_framework.urls')),
    path('auth/token', obtain_auth_token, name='token'),
]
