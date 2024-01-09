from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser

from app.models import File
from app.serializers import ImageResizeSerializer


# Create your views here.
class ImageResizeCreateView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = ImageResizeSerializer
