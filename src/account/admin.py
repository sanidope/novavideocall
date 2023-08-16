from . models import Profile
from django.contrib import admin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_pic', 'smart', 'profile_updated', 'created', 'updated', )
    list_display_links = ('id', 'user',)
