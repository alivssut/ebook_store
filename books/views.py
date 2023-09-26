from django.shortcuts import render
from .models import Ebook
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import EbookSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.

# ebooks list view
class EbookListView(generics.ListAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [SessionAuthentication, TokenAuthentication]