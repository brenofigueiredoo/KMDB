from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    movie_id = serializers.SerializerMethodField()
    critic = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie_id",
            "critic",
        ]

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def get_movie_id(self, obj):
        return obj.movie.id

    def get_critic(self, obj):
        return {
            "id": obj.critic.id,
            "first_name": obj.critic.first_name,
            "last_name": obj.critic.last_name,
        }
