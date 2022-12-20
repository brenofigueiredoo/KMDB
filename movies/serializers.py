from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Movie
from genres.models import Genre
from genres.serializers import GenresSerializer


class MovieSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]

    def create(self, validated_data):
        genr_data = validated_data.pop("genres")

        movie = Movie.objects.create(**validated_data)

        for char in genr_data:
            genr, _ = Genre.objects.get_or_create(**char)
            movie.genres.add(genr)

        return movie
