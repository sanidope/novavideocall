from guidance.views import help_list, help_detail
from django.urls import path, re_path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.index, name='home'),
    path('account/auth/login/', views.login, name='login'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('pricing/', views.pricing, name='pricing'),
    path('download/', views.download_app, name='download_app'),
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
    path('careers/', views.carrers, name='carrers'),
    re_path(r'^careers/detail/(?P<post>[-\w]+)/$', views.carrers_details, name='careers_detail'),
    path('careers/detail/apply/<str:job_position>/', views.carrers_application, name='careers_application'),
    path('help-center/', help_list, name='help_list'),
    re_path(r'^help-center/(?P<classname>[-\w]+)/(?P<post>[-\w]+)/$', help_detail, name='help_detail'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('testimonials/', views.testimonials, name='testimonials'),
    re_path(r'^testimonials/detail/(?P<post>[-\w]+)/$', views.testimonials_details, name='testimonials_details'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('live/videocall/meet/invite/<str:code>/', views.video_invite, name='invite_link'),
    re_path(r'dl/launcher/download/$', views.launcherview, name='launcher'),
    path('download/', views.download_dll, name='download'),
    path('download-app/<str:code>/<str:platform>/', views.download_installer, name='download_installer'),
    path('download-app/<str:platform>/', views.installer, name='installer'),        

]