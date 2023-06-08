from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserDetailsSerializer
from rest_framework import permissions


class UserDetail(generics.RetrieveUpdateAPIView):
    """
    Admin only write view for updating user account details
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailsSerializer
