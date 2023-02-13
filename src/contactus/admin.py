from django.contrib import admin
from . models import (
    PreVisitInquires,
    BillingQuestions,
    SalesQuestions,
    OfficeAddressDetail,
    ContactFormModel
)
# Register your models here.


@admin.register(PreVisitInquires)
class PreVisitInquires(admin.ModelAdmin):
    list_display = ['id', 'user', 'week_day', 'time', 'email']
    list_display_links = ('id', 'user',)


@admin.register(BillingQuestions)
class BillingQuestions(admin.ModelAdmin):
    list_display = ['id', 'user', 'week_day', 'time', 'email']
    list_display_links = ('id', 'user',)

@admin.register(SalesQuestions)
class SalesQuestions(admin.ModelAdmin):
    list_display = ['id', 'user', 'week_day', 'time', 'email']
    list_display_links = ('id', 'user',)

@admin.register(OfficeAddressDetail)
class OfficeAddressDetail(admin.ModelAdmin):
    list_display = ['id', 'user', 'office_pic','office_address']
    list_display_links = ('id', 'user',)

@admin.register(ContactFormModel)
class ContactFormModelAdmin(admin.ModelAdmin):
    list_display = ['id',  'email', 'first_name','last_name', 'message']
    list_display_links = ('id', 'email',)