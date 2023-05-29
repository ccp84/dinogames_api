from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Review model serializer
    Adds read only fields for foreign key models
    Author returns the username for the review writer
    """
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profileicon = serializers.ReadOnlyField(source='author.profileicon')
    # https://www.django-rest-framework.org/api-guide/fields/#datetimefield
    lastupdated = serializers.DateTimeField(format="%d-%m-%Y %H:%M")

    def get_is_author(self, obj):
        """
        Check if the logged in user is the review author
        """
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Review
        fields = [
            'id', 'author', 'is_author', 'profileicon', 'game', 'content', 'lastupdated'
        ]


class ReviewDetailSerializer(ReviewSerializer):
    game = serializers.ReadOnlyField(source='game.title')
