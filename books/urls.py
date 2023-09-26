from django.urls import path
from .views import EbookListView, EbookDetailView

urlpatterns = [
    path("ebooks/", EbookListView.as_view(), name="ebooks_list"),
    path("ebooks/<slug:slug>/", EbookDetailView.as_view(), name="ebook_detail"),
]