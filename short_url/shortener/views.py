from django.views import View
from django.shortcuts import get_object_or_404, redirect

from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import UrlShortener
from .serializers import UrlShortenerCreateSerizliaer, UrlShortenerListSerizliaer, UrlRetrieveUpdateDestroySerializer
from .utils import create_short_url, create_hash_url
from .permissions import IsOwner


class RedirectToFullURL(View):

    def get(self, request, hash_url, *args, **kwargs):
        url_obj = get_object_or_404(UrlShortener, hash_url=hash_url)
        url_obj.click()
        return redirect(url_obj.default_url)


class URLCreateShortUrlView(generics.CreateAPIView):
    queryset = UrlShortener.objects.all()
    serializer_class = UrlShortenerCreateSerizliaer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        default_url = self.request.data['default_url']
        hash_url = create_hash_url(default_url)
        short_url = create_short_url(hash_url)
        return serializer.save(user=user, short_url=short_url, hash_url=hash_url)
    

class URLListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UrlShortenerListSerizliaer

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = UrlShortener.objects.all()
        else:
            queryset = UrlShortener.objects.filter(user=self.request.user)
        return queryset


class URLRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UrlRetrieveUpdateDestroySerializer
    queryset = UrlShortener.objects.all()
    permission_classes = [permissions.IsAdminUser|IsOwner]
    
    def update(self, request, *args, **kwargs):
        default_url = self.request.data['default_url']
        hash_url = create_hash_url(default_url)

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        
        instance.hash_url = hash_url
        instance.short_url = create_short_url(hash_url)
        instance.save()

        return Response(serializer.data)
