from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MediaLinks(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    discord = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "MediaLinks"

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'MediaLinks'
