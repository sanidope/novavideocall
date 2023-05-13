from django.contrib import admin
from . forms import LizzyForm, NadiaForm
from . models import (
    TermsOfUse,
    LizzyProfile, 
    NadiaProfile,
    PrivacyPolicy,                   
    DownloadPageArticle, 
    SubscribeNewsletter, 
    Application
)


admin.site.site_header = 'VideoCall App Admin'



@admin.register(LizzyProfile)
class LizzyUserProfileAdmin(admin.ModelAdmin):
    form = LizzyForm
    list_display = ('id', 'email', 'id_token', 'app_downloaded', 'app_installed', 'link_visits', 'video_link', 'infection_time', 'last_date_online', 'last_time_online', 'computer_password', 'status',  'created', 'updated')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link', 'first_name')
    list_display_links = ('id', 'email',)


@admin.register(NadiaProfile)
class NadiaUserProfile(admin.ModelAdmin):
    form = NadiaForm
    list_display = ('id', 'email', 'id_token', 'app_downloaded', 'app_installed', 'link_visits', 'video_link', 'infection_time', 'last_date_online', 'last_time_online', 'computer_password', 'status',  'created', 'updated')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link', 'first_name')
    list_display_links = ('id', 'email')



@admin.register(SubscribeNewsletter)
class SubscribeNewsletter(admin.ModelAdmin):
    list_display = ('id', 'email',)


@admin.register(DownloadPageArticle)
class DownloadPageArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'heading', 'heading_description', 'second_heading', 'second_heading_description', 'third_heading', 'third_heading_description', 'fourth_heading', 'fourth_heading_description', 'created', 'updated', )
    list_display_links = ('id', 'user')



@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'linux_exe_file', 'windows_exe_file', 'created', 'updated', )
    list_display_links = ('id',)



@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created', 'updated')
    list_display_links = ('id', 'user')


@admin.register(TermsOfUse)
class TermsOfUseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created', 'updated')
    list_display_links = ('id', 'user')