from rest_framework import generics
from .models import Game
from .serializers import GameSerializer
from rest_framework import permissions


class GameList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
