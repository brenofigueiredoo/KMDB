from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import MovieSerializer
from .models import Movie
from .permissions import isSuperUser
import ipdb


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isSuperUser]

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, genres=self.request.data["genres"])
