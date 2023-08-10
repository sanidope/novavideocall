from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from publishapp.sitemaps import BlogSiteMaps
from careers.sitemaps import CareerSiteMaps
from . sitemaps import StaticViewSitemap
from guidance.sitemaps import (
    PaymentSiteMaps, MyAccountsSiteMaps,
    PurchasingSiteMaps, ProfilePlanSiteMaps,
    SupportPlanSiteMaps, MorePlanSiteMaps
)
from testimonials.sitemaps import CustomerStoriesSiteMaps
from django.urls import path, include, re_path
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView


sitemaps = {
    'posts' : BlogSiteMaps,
    'careers' : CareerSiteMaps,
    'testimonials' : CustomerStoriesSiteMaps,    
    'guidance_payment' : PaymentSiteMaps,
    'guidance_myaccounts' : MyAccountsSiteMaps,
    'guidance_purchasing' : PurchasingSiteMaps,
    'guidance_profileplan' : ProfilePlanSiteMaps,
    'guidance_supportplan' : SupportPlanSiteMaps,
    'guidance_moreplan' : MorePlanSiteMaps,
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('admin/secret-admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('blog/', include('publishapp.urls', namespace='publishapp')),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="videocall/robots.txt", content_type='text/plain')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = views.error_404_view
handler500 = views.error_500_view