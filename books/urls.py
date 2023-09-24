from django.urls import path
from .views import EbookListView

urlpatterns = [
    path("ebooks/<slug:slug>/", EbookListView.as_view(), name="ebooks_list"),
]