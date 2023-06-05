from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """
    Rating model serializer
    Adds read only fields for foreign key models
    Author returns the username for the rating owner
    """
    author = serializers.ReadOnlyField(source='author.username')
    game_title = serializers.ReadOnlyField(source='game.title')

    class Meta:
        model = Rating
        fields = [
            'id', 'author', 'game', 'game_title', 'rating'
        ]

    def create(self, validated_data):
        """
        Return an error message instead of 500 for duplicate ratings
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You can only rate a game once'
            })
