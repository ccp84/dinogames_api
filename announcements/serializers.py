from rest_framework import serializers
from .models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    """
    Announcement model serializer
    Adds read only fields for foreign key models
    Author returns the username for the announcement writer
    """
    author = serializers.ReadOnlyField(source='author.username')
    profileicon = serializers.ReadOnlyField(source='author.profileicon')
    lastupdated = serializers.SerializerMethodField()
    category_title = serializers.ReadOnlyField(source='category.title')

    def get_lastupdated(self, obj):
        """
        Returns a readable format for the 'lastupdated' field.
        """
        return obj.lastupdated.strftime("%d-%m-%Y %H:%M")

    class Meta:
        model = Announcement
        fields = [
            'id', 'category', 'category_title', 'title', 'content', 'lastupdated', 'author', 'profileicon'
        ]
