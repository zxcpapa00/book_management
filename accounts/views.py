from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import UserSerializer

user_model = get_user_model()


class RegistrationUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = user_model.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_model.objects.create_user(
                username=serializer.data['username'],
                password=serializer.data['password'],
                first_name=serializer.data['first_name'],
                email=serializer.data['email']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
