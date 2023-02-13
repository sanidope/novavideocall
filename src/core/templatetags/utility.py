import datetime
from django import template
from socialmedialinks.models import MediaLinks

register = template.Library()


@register.simple_tag()
def current_year():
    tday = datetime.date.today()
    return str(tday.year)


@register.simple_tag()
def get_twitter_link():
    twitter_link = MediaLinks.objects.get(user__username = 'nadia')
    return twitter_link.twitter


@register.simple_tag()
def get_instagram_link():
    instagram_link = MediaLinks.objects.get(user__username = 'nadia')
    return instagram_link.instagram


@register.simple_tag()
def get_youtube_link():
    youtube_link = MediaLinks.objects.get(user__username = 'nadia')
    return youtube_link.youtube


@register.simple_tag()
def get_discord_link():
    discord_link = MediaLinks.objects.get(user__username = 'nadia')
    return discord_link.discord
