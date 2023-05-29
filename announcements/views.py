from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework import permissions


class AnnouncementList(generics.ListAPIView):
    """
    Readonly endpoint for listing announcements
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class AnnouncementCreate(generics.ListCreateAPIView):
    """
    Read write endpoint for admin users to create new announcements
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Read write delete endpoint for admin. Udates the author on save
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
