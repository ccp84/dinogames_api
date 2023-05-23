from rest_framework import generics
from .models import Game
from .serializers import GameSerializer
from rest_framework import permissions
from dinogames.permissions import IsOwnerOrReadOnly


class GameList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OwnerList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GameSerializer

    def get_queryset(self):
        """
        Override the standard query set and filter
        """
        user = self.request.user
        return Game.objects.filter(owner=user)


class OwnerEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
