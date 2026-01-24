from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from users.serilizers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.contrib.auth.models import User
from home.serializers import UserSerializer
# Create your views here.


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]


class CreateUserAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
    
class UpdateUserAPIView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    
class DeleteUserAPIView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    
class DetailUserAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'