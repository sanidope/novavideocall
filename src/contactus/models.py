from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField



class PreVisitInquires(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, default=1)
    week_day = models.CharField(max_length=1000, default='Mon-Fri')
    time = models.CharField(max_length=1000)
    email = models.EmailField()

    def __str__(self):
        return "PrevisitInquires"


    class Meta:
        verbose_name_plural = "PreVisitInquires"



class BillingQuestions(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, default=1)
    week_day = models.CharField(max_length=1000, default='Mon-Fri')
    time = models.CharField(max_length=1000)
    email = models.EmailField()


    def __str__(self):
        return "SalesQuestion"

    class Meta:
        verbose_name_plural = "BillingQuestions"



class SalesQuestions(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, default=1)
    week_day = models.CharField(max_length=1000, default='Mon-Fri')
    time = models.CharField(max_length=1000)
    email = models.EmailField()


    def __str__(self):
        return "SalesQuestion"

    class Meta:
        verbose_name_plural = "SalesQuestions"



class ContactFormModel(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.email

    
    class Meta:
        verbose_name_plural = "ContactFormModel"

 

class OfficeAddressDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, default=1)
    office_pic = ProcessedImageField(upload_to="office_pic/%y/%m/%d", processors=[ResizeToFill(474, 392)],  format='JPEG', options={'quality': 60} )
    office_pic_description = models.CharField(max_length=500, default='Image Description')
    country_code = models.CharField(max_length=100, default='UK')
    office_address = HTMLField()


    class Meta:
        verbose_name_plural = "OfficeAddressDetails"


    def __str__(self):
        return "OfficeAddressDetails"


