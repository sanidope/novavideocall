from django.contrib import admin
from . models import (PrivacyPolicy, TermsOfUse)


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created', 'updated')
    list_display_links = ('id', 'user')


@admin.register(TermsOfUse)
class TermsOfUseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'created', 'updated')
    list_display_links = ('id', 'user')

