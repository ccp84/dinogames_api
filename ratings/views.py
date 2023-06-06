from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Rating
from .serializers import RatingSerializer
from rest_framework import permissions
from dinogames.permissions import IsOwnerOrReadOnly


class RatingList(generics.ListCreateAPIView):
    """
    Read and write endpoint for all authenticated members
    Logged in members can add a new rating
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,]
    filterset_fields = ['game', 'author']

    ordering_fields = [
        'game'
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Read edit and destroy endpoint for authenticated members
    Instance owner can ammend their rating
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
