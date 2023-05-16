from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Game
        fields = [
            'id', 'owner', 'title', 'tags', 'minplayers',
            'maxplayers', 'playtime'
        ]
