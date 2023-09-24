from rest_framework import serializers
from .models import Ebook


class EbookSerializer(serializers.ModelSerializer):    
    class Meta:
        fields = '__all__'
        model = Ebook
        lookup_field = 'slug'