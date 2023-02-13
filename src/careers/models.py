from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth.models import User 


class FirstRow(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_text = models.CharField(max_length=1000)
    second_text = models.CharField(max_length=1000)
    third_text = models.CharField(max_length=1000)


class SecondRow(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    first_text = models.CharField(max_length=1000)
    first_text_subtitle = models.CharField(max_length=1000)
    second_text = models.CharField(max_length=1000)
    second_text_subtitle = models.CharField(max_length=1000)
    third_text = models.CharField(max_length=1000)
    third_text_subtitle = models.CharField(max_length=1000)
    fourth_text = models.CharField(max_length=1000)
    fourth_text_subtitle = models.CharField(max_length=1000)


class ThirdRow(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    first_text = models.CharField(max_length=1000)
    first_text_subtext = models.CharField(max_length=1000)
    second_text = models.CharField(max_length=1000)
    second_text_subtext = models.CharField(max_length=1000)
    third_text = models.CharField(max_length=1000)
    third_text_subtext = models.CharField(max_length=1000)
    fourth_text = models.CharField(max_length=1000)
    fourth_text_subtext = models.CharField(max_length=1000)


class FourthRow(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    first_text = models.CharField(max_length=1000)
    first_text_subtext = models.CharField(max_length=1000)
    second_text = models.CharField(max_length=1000)
    second_text_subtext = models.CharField(max_length=1000)
    third_text = models.CharField(max_length=1000)
    third_text_subtext = models.CharField(max_length=1000)
    fourth_text = models.CharField(max_length=1000)
    fourth_text_subtext = models.CharField(max_length=1000)
    fifth_text = models.CharField(max_length=1000)
    fifth_text_subtext = models.CharField(max_length=1000)  
    sixth_text = models.CharField(max_length=1000)
    sixth_text_subtext = models.CharField(max_length=1000)


class FifthRow(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    heading = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)


class SixthRow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    job_title = models.CharField(max_length=1000)
    slug =  models.SlugField(max_length=250, unique_for_date='created', null=True)
    application_deadline = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=1000)
    employment_type = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    compensation = models.CharField(max_length=1000)
    body = HTMLField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'SixthRow'


    def get_absolute_url(self):
        return reverse("core:careers_detail", args=[
            self.slug
        ])
    
