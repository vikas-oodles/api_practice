from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, permissions
from django.contrib.auth.models import User
from . models import Profile, Address
from myapi.serializers import UserSerializer, ProfileSerializer

# Create your views here.
class UserListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer