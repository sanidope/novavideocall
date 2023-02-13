import os
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from imagekit.models import  ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class CustomerStories(models.Model):
 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    company_logo = ProcessedImageField(upload_to='Customerstories/companylogo/%y/%m/%d', processors=[ResizeToFill(91, 30)],  format='png', options={'quality': 60})
    company_picture_large = ProcessedImageField(upload_to="Customerstories/%y/%m/%d", processors=[ResizeToFill(900, 600)],  format='JPEG', options={'quality': 60})
    company_picture_small = ImageSpecField(source='company_picture_large', processors=[ResizeToFill(356, 295)], format='JPEG', options={'quality': 60})
    company_picture_description = models.CharField(max_length=500, default='Image Description')
    testimonal_title = models.CharField(max_length=4000)
    slug =  models.SlugField(max_length=250, unique_for_date='created', null=True)
    testimonal_subtitle = models.CharField(max_length=4000, blank=True, null=True)
    body = HTMLField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'CustomerStories'

    def __str__(self):
        return "CustomerStories"

    
    def get_absolute_url(self):
        return reverse("core:testimonials_details", args=[
            self.slug
        ])
    


class BlockQuote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_logo_img = models.FileField(upload_to="Customerstories/blackquote/%y/%m/%d")
    quote = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)

    
    def __str__(self):
        return "BlockQuote"


