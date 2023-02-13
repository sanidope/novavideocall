from django.contrib import admin
from .models import (
    FirstRow, SecondRow,
    ThirdRow, FourthRow,
    FifthRow, SixthRow, 
)


@admin.register(FirstRow)
class FirstRowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_text', 'second_text', 'third_text')
    list_display_links = ('id', 'user')


@admin.register(SecondRow)
class SecondRowAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'heading', 'subtitle', 'first_text', 'first_text_subtitle', 'second_text', 'second_text_subtitle', 'third_text', 'third_text_subtitle', 'fourth_text', 'fourth_text_subtitle', )
    list_display_links = ('id', 'user')


@admin.register(ThirdRow)
class ThirdRowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'heading', 'subtitle', 'first_text', 'first_text_subtext', 'second_text', 'second_text_subtext', 'third_text', 'third_text_subtext', 'fourth_text', 'fourth_text_subtext', )
    list_display_links = ('id', 'user')


@admin.register(FourthRow)
class FourthRowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'heading', 'subtitle', 'first_text', 'first_text_subtext', 'second_text', 'second_text_subtext', 'third_text', 'third_text_subtext', 'fourth_text', 'fourth_text_subtext', 'fifth_text', 'fifth_text_subtext', 'sixth_text', 'sixth_text_subtext', )
    list_display_links = ('id', 'user')


@admin.register(FifthRow)
class FifthRowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'heading', 'title', )
    list_display_links = ('id', 'user')


@admin.register(SixthRow)
class SixthRowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job_title', 'slug', 'application_deadline', 'department', 'employment_type', 'location', 'compensation', 'body', 'created', 'updated',)
    list_display_links = ('id', 'user')
    prepopulated_fields = {'slug': ('job_title',)}
