from rest_framework import serializers
from .models import Game
from ratings.models import Rating


class GameSerializer(serializers.ModelSerializer):
    """
    Rating id links rating to the member who created it
    """
    rating_id = serializers.SerializerMethodField()
    rating_value = serializers.SerializerMethodField()
    thumbsup = serializers.ReadOnlyField()
    thumbsdown = serializers.ReadOnlyField()

    def get_rating_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                author=user, game=obj
            ).first()
            return rating.id if rating else None
        return None

    def get_rating_value(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                author=user, game=obj
            ).first()
            return rating.rating if rating else None
        return None

    class Meta:
        model = Game
        fields = [
            'id', 'title', 'tags', 'minplayers',
            'maxplayers', 'playtime', 'overview', 'rating_id', 'rating_value', 'thumbsup', 'thumbsdown',
        ]
