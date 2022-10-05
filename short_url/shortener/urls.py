from django.urls import path

from .views import URLCreateShortUrlView, URLListView, URLRetrieveUpdateDestroyView

urlpatterns = [
    path('create-short-url/', URLCreateShortUrlView.as_view()),
    path('list/urls/', URLListView.as_view()),
    path('url/<int:pk>/', URLRetrieveUpdateDestroyView.as_view())
]