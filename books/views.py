from django.shortcuts import render
from .models import Ebook
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import EbookSerializer
from rest_framework import generics

# Create your views here.

# ebooks list view
class EbookListView(generics.ListAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [AllowAny,]