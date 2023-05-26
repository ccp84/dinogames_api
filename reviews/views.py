from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from rest_framework import permissions
from dinogames.permissions import IsOwnerOrReadOnly


class ReviewList(generics.ListCreateAPIView):
    """
    Read and write endpoint for all authenticated members
    Logged in members can create new reviews
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'game']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Read write delete endpoint for review author
    Permission class locks down write and delete access
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()
