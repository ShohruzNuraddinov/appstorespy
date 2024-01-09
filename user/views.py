from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from user import serializers

# Create your views here.


class RegisterCreateView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    queryset = User.objects.all()


class LoginView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer
    queryset = User.objects.all()
