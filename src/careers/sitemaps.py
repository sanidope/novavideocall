from django.contrib.sitemaps import Sitemap
from .models import SixthRow


class CareerSiteMaps(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return SixthRow.objects.all()

    def lastmod(self, obj):
        return obj.created 