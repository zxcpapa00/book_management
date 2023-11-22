from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', include('book.urls')),
    path('api/v1/account/', include('accounts.urls')),
]
