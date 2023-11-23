from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth-drf/', include('rest_framework.urls')),
    path('auth/token', obtain_auth_token, name='token'),
]
