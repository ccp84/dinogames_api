from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserDetailsSerializer
from rest_framework import permissions


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Read write view for updating user account details
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailsSerializer
