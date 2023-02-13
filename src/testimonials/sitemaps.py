from django.contrib.sitemaps import Sitemap
from .models import CustomerStories


class CustomerStoriesSiteMaps(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return CustomerStories.objects.all()

    def lastmod(self, obj):
        return obj.created 
