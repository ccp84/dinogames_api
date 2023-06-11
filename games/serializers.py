from rest_framework import serializers
from .models import Game
from ratings.models import Rating


class GameSerializer(serializers.ModelSerializer):
    """
    Return fields for all Game model endpoint views
    """
    rating_id = serializers.SerializerMethodField()
    rating_value = serializers.SerializerMethodField()
    thumbsup = serializers.ReadOnlyField()
    thumbsdown = serializers.ReadOnlyField()
    playtime_name = serializers.SerializerMethodField()

    def get_rating_id(self, obj):
        """
        Return the id of the rating created for the game by the
        currently logged in user, otherwise returns None if no rating
        is found
        """
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                author=user, game=obj
            ).first()
            return rating.id if rating else None
        return None

    def get_rating_value(self, obj):
        """
        Return the value of the rating currently being viewed
        Ratings are unique per user so only one value can be shown
        per logged in user
        """
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                author=user, game=obj
            ).first()
            return rating.rating if rating else None
        return None

    def get_playtime_name(self, obj):
        """
        Return the human readable value of the GAME_LENGTH_CHOICES tuple
        to the serializer for use by the React frontend
        """
        return obj.get_playtime_display()

    class Meta:
        model = Game
        fields = [
            'id', 'title', 'tags', 'minplayers',
            'maxplayers', 'playtime', 'playtime_name', 'overview',
            'rating_id', 'rating_value', 'thumbsup', 'thumbsdown',
        ]
