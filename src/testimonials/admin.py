from . models import CustomerStories, BlockQuote
from django.contrib import admin



@admin.register(CustomerStories)
class CustomerStoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company_logo', 'company_picture_small', 'company_picture_large', 'testimonal_title', 'slug', 'body', 'created', 'updated')
    list_display_links = ('id', 'user')
    prepopulated_fields = {'slug': ('testimonal_title',)}


@admin.register(BlockQuote)
class BlockQuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company_logo_img', 'quote', 'name', 'title', )
    list_display_links = ('id', 'user')