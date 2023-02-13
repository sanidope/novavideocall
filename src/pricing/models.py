from tinymce.models import HTMLField
from django.db import models
from django.contrib.auth.models import User 


class PricingHeading(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    heading = models.CharField(max_length=1000)

    def __str__(self):
        return "Pricing Heading"



class TeamsPlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    sub_heading = models.CharField(max_length=1000)
    pricing = models.DecimalField(max_digits=8, decimal_places=2)
    feature_1 = models.CharField(max_length=1000)
    feature_2 = models.CharField(max_length=1000)
    feature_3 = models.CharField(max_length=1000)
    feature_4 = models.CharField(max_length=1000)
    feature_5 = models.CharField(max_length=1000)
    feature_6 = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return "BasicPlan"

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = "TeamsPlan"
        

class PricingFAQ(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    question_1 = models.CharField(max_length=4000)
    answer_1 = HTMLField()
    question_2 = models.CharField(max_length=4000)
    answer_2 = HTMLField()
    question_3 = models.CharField(max_length=4000)
    answer_3 = HTMLField()
    question_4 = models.CharField(max_length=4000)
    answer_4 = HTMLField()
    question_5 = models.CharField(max_length=4000, null=True)
    answer_5 = HTMLField(null=True)
    question_6 = models.CharField(max_length=4000, null=True)
    answer_6 = HTMLField(null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Pricing FAQ"

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = "PricingFAQs"


class ProfessionalPlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    sub_heading = models.CharField(max_length=1000)
    pricing = models.DecimalField(max_digits=8, decimal_places=2)
    feature_1 = models.CharField(max_length=1000)
    feature_2 = models.CharField(max_length=1000)
    feature_3 = models.CharField(max_length=1000)
    feature_4 = models.CharField(max_length=1000)
    feature_5 = models.CharField(max_length=1000)
    feature_6 = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return "ProfessionalPlan"

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = "ProfessionalPlan"




class PricingComparePlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    feature = models.CharField(max_length=1000, null=True)
    professional = models.BooleanField(default=False)
    teams = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "PricingComparePlan"

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'PricingComparePlans'


class HighLightSection(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    heading = models.CharField(max_length=1000)
    description = models.CharField(max_length=4000)
    testimonial = models.CharField(max_length=1000)
    user_full_name = models.CharField(max_length=1000)
    user_pic = models.ImageField(upload_to="Pricing/images/%y/%m/%d", blank=True, null=True)
    user_title = models.CharField(max_length=1000)
    first_status = models.CharField(max_length=1000)
    first_status_desc = models.CharField(max_length=1000)
    second_status = models.CharField(max_length=1000)
    second_status_desc = models.CharField(max_length=1000)
    third_status = models.CharField(max_length=1000)
    third_status_desc = models.CharField(max_length=1000)
    fourth_status = models.CharField(max_length=1000)
    fourth_status_desc = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "HighLightSection"

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'HighLightSection'

