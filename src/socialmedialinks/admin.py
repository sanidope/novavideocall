from django.contrib import admin
from . models import MediaLinks


@admin.register(MediaLinks)
class MediaLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'discord', 'twitter', 'instagram', 'youtube', 'created', 'updated')
    list_display_links = ('id', 'user')