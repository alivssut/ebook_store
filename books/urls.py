from django.urls import path
from .views import EbookListView

urlpatterns = [
    path("ebooks/", EbookListView.as_view(), name="ebooks_list"),
]