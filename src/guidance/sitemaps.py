from django.contrib.sitemaps import Sitemap
from .models import (
    Payment, MyAccounts, Purchasing,
    ProfilePlan, Support, More
)


class PaymentSiteMaps(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Payment.objects.all()

    def lastmod(self, obj):
        return obj.created 


class MyAccountsSiteMaps(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return MyAccounts.objects.all()

    def lastmod(self, obj):
        return obj.created 


class PurchasingSiteMaps(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Purchasing.objects.all()

    def lastmod(self, obj):
        return obj.created 


class ProfilePlanSiteMaps(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ProfilePlan.objects.all()

    def lastmod(self, obj):
        return obj.created 


class SupportPlanSiteMaps(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Support.objects.all()

    def lastmod(self, obj):
        return obj.created 


class MorePlanSiteMaps(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return More.objects.all()

    def lastmod(self, obj):
        return obj.created 


