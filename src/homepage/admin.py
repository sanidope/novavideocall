from django.contrib import admin
from . models import (
    SecondColumn,
    ThirdColumn, FourthColumn,
    FifthColumn, SixthColumn
)


@admin.register(SecondColumn)
class SecondColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_text', 'second_text', 'third_text', 'fourth_text')
    list_display_links = ('id', 'user')


@admin.register(ThirdColumn)
class ThirdColumn(admin.ModelAdmin):
    list_display = ('id', 'user', 'heading', 'subtitle', 'first_text', 'second_text', 'third_text', 'fourth_text', 'fifth_text', 'sixth_text')
    list_display_links = ('id', 'user')

@admin.register(FourthColumn)
class FourthColumn(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_text', 'second_text', 'third_text', 'fourth_text', 'fifth_text', 'sixth_text')
    list_display_links = ('id', 'user')

@admin.register(FifthColumn)
class FifthColumn(admin.ModelAdmin):
    list_display = ('id', 'user', 'heading', 'subtitle', 'first_text', 'second_text', 'third_text')
    list_display_links = ('id', 'user')

@admin.register(SixthColumn)
class SixthColumn(admin.ModelAdmin):
    list_display = ('id', 'user', 'heading', 'subtitle', 'comment', 'fullname', 'picture', 'title', 'first_text', 'first_text_subtitle',  'second_text', 'second_text_subtitle', 'third_text',  'third_text_subtitle', 'fourth_text', 'fourth_text_subtitle')
    list_display_links = ('id', 'user')