from django.contrib import admin
from . models import (
    Payment, MyAccounts,
    Purchasing, ProfilePlan,
    Support, More
)

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'slug', 'body', 'created', 'update')
    list_display_links = ('id', 'user')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(MyAccounts)
class MyAccountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'slug', 'body', 'created', 'update')
    list_display_links = ('id', 'user')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Purchasing)
class PurchasingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'slug', 'body', 'created', 'update')
    list_display_links = ('id', 'user')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProfilePlan)
class ProfilePlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'slug', 'body', 'created', 'update')
    list_display_links = ('id', 'user')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'slug', 'body', 'created', 'update')
    list_display_links = ('id', 'user')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(More)
class MoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'slug', 'body', 'created', 'update')
    list_display_links = ('id', 'user')
    prepopulated_fields = {'slug': ('title',)}