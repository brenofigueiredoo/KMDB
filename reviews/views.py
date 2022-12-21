from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import isCriticOrIsAdm
from .serializers import ReviewSerializer
from .models import Review
from movies.models import Movie
from django.shortcuts import get_object_or_404


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isCriticOrIsAdm]

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        movie_id = self.kwargs["movie_id"]
        movie = get_object_or_404(Movie, id=movie_id)
        return serializer.save(critic=self.request.user, movie=movie)
