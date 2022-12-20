from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import User
from .permissions import isAdminListUser
from .serializers import UserSerializer
import ipdb


class UserView(generics.ListCreateAPIView, PageNumberPagination):

    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminListUser]

    serializer_class = UserSerializer
    queryset = User.objects.all()
