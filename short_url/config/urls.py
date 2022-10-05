from django.contrib import admin
from django.urls import path, include

from shortener.views import RedirectToFullURL

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('shortener.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('<slug:hash_url>/', RedirectToFullURL.as_view())
]
