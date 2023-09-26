from django.shortcuts import render
from .models import Ebook
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import EbookSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.

# ebooks list view
class EbookListView(generics.ListAPIView):
    serializer_class = EbookSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Ebook.objects.all_ebooks(active=True)

# ebook detail view
class EbookDetailView(generics.RetrieveAPIView):
    serializer_class = EbookSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated,]
    lookup_url_kwarg  = 'slug'
    lookup_field = 'slug'
    queryset = Ebook.objects.all_ebooks(active=True)