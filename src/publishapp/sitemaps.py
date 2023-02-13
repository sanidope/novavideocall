from django.contrib.sitemaps import Sitemap
from .models import Posts


class BlogSiteMaps(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Posts.published.all()

    def lastmod(self, obj):
        return obj.publish 