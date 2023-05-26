from rest_framework import generics, filters
from .models import Game
from .serializers import GameSerializer
from rest_framework import permissions


class GameList(generics.ListAPIView):
    """
    Read only view accessible to all.
    Filter and search options for game library frontend
    """
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


class GameDetail(generics.RetrieveAPIView):
    """
    Read only view for detailed game view
    Accessible to all
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class GameCreate(generics.ListCreateAPIView):
    """
    Admin only read write view for game creation
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class GameEdit(generics.RetrieveUpdateDestroyAPIView):
    """
    Admin only edit and delete view
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
