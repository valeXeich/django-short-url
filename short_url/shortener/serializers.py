from rest_framework import serializers

from .models import UrlShortener


class UrlShortenerCreateSerizliaer(serializers.ModelSerializer):
    class Meta:
        model = UrlShortener
        fields = ['default_url', 'user', 'short_url', 'hash_url']
        read_only_fields = ['user', 'hash_url', 'short_url']


class UrlShortenerListSerizliaer(serializers.ModelSerializer):
    class Meta:
        model = UrlShortener
        fields = ['short_url', 'clicked']
    

class UrlRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlShortener
        fields = ['default_url', 'clicked']
        read_only_fields = ['clicked']