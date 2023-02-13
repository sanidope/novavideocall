from django.contrib import admin
from . models import (
    TeamsPlan,
    PricingFAQ,
    PricingHeading,
    ProfessionalPlan,
    PricingComparePlan,
    HighLightSection,
)


@admin.register(PricingHeading)
class PricingHeadingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'heading')
    list_display_links = ('id', 'user',)


@admin.register(TeamsPlan)
class TeamsPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sub_heading', 'pricing', 'feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5', 'feature_6', 'created', 'updated')
    list_display_links = ('id', 'user',)



@admin.register(PricingFAQ)
class PricingFAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question_1', 'answer_1','question_2', 'answer_2','question_3', 'answer_3','question_4', 'answer_4', 'question_5', 'answer_5', 'question_6', 'answer_6','created', 'updated')
    list_display_links = ('id', 'user',)



@admin.register(ProfessionalPlan)
class ProfessionalPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sub_heading', 'pricing', 'feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5', 'feature_6', 'created', 'updated')
    list_display_links = ('id', 'user',)

@admin.register(HighLightSection)
class HighLightSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'heading', 'description', 'testimonial', 'user_full_name', 'user_pic', 'user_title', 'first_status', 'first_status_desc', 'second_status', 'second_status_desc', 'third_status', 'third_status_desc', 'fourth_status', 'fourth_status_desc', 'created', 'updated')
    list_display_links = ('id', 'user',)

@admin.register(PricingComparePlan)
class PricingComparePlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'feature', 'professional', 'teams', 'created', 'updated')
    list_display_links = ('id', 'user',)