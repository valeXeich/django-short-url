from django.db import models
from django.contrib.auth.models import User


class UrlShortener(models.Model):
    default_url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)
    hash_url = models.CharField(max_length=255)
    clicked = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')

    def click(self):
        self.clicked += 1
        self.save()

    def __str__(self) -> str:
        return f'Owner: {self.user.username}, short url: {self.short_url}'
