from django.contrib import admin
from . models import * 


@admin.register(FirstSection)
class FirstSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'about_pic', 'created', 'updated']
    list_display_links = ('id', 'user',)


@admin.register(SecSection)
class SecondSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title1', 'content1',  'title2', 'content2', 'title3', 'content3', 'title4', 'content4', 'created', 'updated']
    list_display_links = ('id', 'user',)



@admin.register(FourthSection)
class FourthSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'content', 'created', 'updated']
    list_display_links = ('id', 'user',)

@admin.register(FifthSection)
class FifthSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'leadername1', 'leadertitle1', 'leaderpic1', 'leadername2', 'leadertitle2', 'leaderpic2', 'leadername3', 'leadertitle3', 'leaderpic3',  'created', 'updated']
    list_display_links = ('id', 'user',)


@admin.register(AboutUsIcons)
class AboutUsIconsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'pic1', 'pic1_description', 'pic2', 'pic2_description', 'pic3', 'pic3_description', 'pic4', 'pic4_description', 'pic5', 'pic5_description', 'pic6', 'pic6_description', 'pic7', 'pic7_description', 'created', 'updated']
    list_display_links = ('id', 'user',)
