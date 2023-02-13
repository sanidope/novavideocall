from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['core:home', 'core:about_us', 'core:contact_us', 'core:pricing', 'core:terms_of_use', 'core:login', 'core:privacy_policy', 'core:download_app']

    def location(self, item):
        return reverse(item)
