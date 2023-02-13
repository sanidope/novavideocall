
from .models import Posts, AboutAuthor
from django.contrib import admin


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'slug', 'publish','post_image', 'post_image_description', 'status')
    list_filter = ('status',  'created', 'publish', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Posts, PostsAdmin)



@admin.register(AboutAuthor)
class AboutAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'author_pic', 'author_pic_description', 'description')
    list_display_links = ('id', 'user')