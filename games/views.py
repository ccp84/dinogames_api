from rest_framework import generics, filters
from .models import Game
from .serializers import GameSerializer
from rest_framework import permissions
from dinogames.permissions import IsOwnerOrReadOnly


class GameList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.all().order_by('-id')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'title',
        'tags',
    ]
    ordering_fields = [
        'id',
        'title',
        'maxplayers',
        'minplayers',
        'playtime',
    ]


class GameDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class GameEdit(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
