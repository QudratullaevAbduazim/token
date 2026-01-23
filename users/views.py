from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serilizers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.contrib.auth.models import User
from .serilizers import UserSerializer

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "username va password kerak"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "bunday user bor"}, status=400)

        user = User.objects.create_user(
            username=username,
            password=password
        )

        token = Token.objects.create(user=user)

        return Response({
            "message": "user yaratildi",
            "token": token.key
        })




class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "login xato"}, status=400)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    




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