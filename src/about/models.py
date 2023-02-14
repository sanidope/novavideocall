from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class FirstSection(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    about_text = models.TextField()
    about_pic = models.ImageField(upload_to="about_pic/%y/%m/%d")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "First Section"
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'FirstSection'


class SecSection(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    title1 = models.CharField(max_length=1000)
    content1 = HTMLField()
    title2 = models.CharField(max_length=1000)
    content2 = HTMLField()
    title3 = models.CharField(max_length=1000)
    content3 = HTMLField()
    title4 = models.CharField(max_length=1000)
    content4 = HTMLField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Second Section"
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'SecondSection'




class FourthSection(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=1000, null=True)
    content = HTMLField(null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return "Fourth Section"
    

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Foruth Section'



class FifthSection(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    leadername1 = models.CharField(max_length=100, null=True)
    leadertitle1 = models.CharField(max_length=100, null=True)
    leaderpic1 = ProcessedImageField(upload_to="about_pic/leadership/%y/%m/%d", processors=[ResizeToFill(231, 231)], format='JPEG', options={'quality': 60}, null=True)
    leaderpic1_description = models.CharField(max_length=500, default='Image Description')
    leadername2 = models.CharField(max_length=100, null=True)
    leadertitle2 = models.CharField(max_length=100, null=True)
    leaderpic2 = ProcessedImageField(upload_to="about_pic/leadership/%y/%m/%d", processors=[ResizeToFill(231, 231)], format='JPEG', options={'quality': 60}, null=True)
    leaderpic2_description = models.CharField(max_length=500, default='Image Description')
    leadername3 = models.CharField(max_length=100, null=True)
    leadertitle3 = models.CharField(max_length=100, null=True)
    leaderpic3 = ProcessedImageField(upload_to="about_pic/leadership/%y/%m/%d", processors=[ResizeToFill(231, 231)], format='JPEG', options={'quality': 60}, null=True)
    leaderpic3_description = models.CharField(max_length=500, default='Image Description')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Fifth Section"
    

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Fifth Section'



class AboutUsIcons(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True)
    pic1 = ProcessedImageField(upload_to="about_pic/icons/%y/%m/%d", processors=[ResizeToFill(42, 42)], format='png', options={'quality': 60}, null=True, blank=True)
    pic1_description = models.CharField(max_length=500, default='Image Description', null=True, blank=True)
    pic2 = ProcessedImageField(upload_to="about_pic/icons/%y/%m/%d", processors=[ResizeToFill(42, 42)], format='png', options={'quality': 60}, null=True, blank=True)
    pic2_description = models.CharField(max_length=500, default='Image Description', null=True, blank=True)
    pic3 = ProcessedImageField(upload_to="about_pic/icons/%y/%m/%d", processors=[ResizeToFill(42, 42)], format='png', options={'quality': 60}, null=True, blank=True)
    pic3_description = models.CharField(max_length=500, default='Image Description', null=True, blank=True)
    pic4 = ProcessedImageField(upload_to="about_pic/icons/%y/%m/%d", processors=[ResizeToFill(42, 42)], format='png', options={'quality': 60}, null=True, blank=True)
    pic4_description = models.CharField(max_length=500, default='Image Description', null=True, blank=True)
    pic5 = ProcessedImageField(upload_to="about_pic/icons/%y/%m/%d", processors=[ResizeToFill(42, 42)], format='png', options={'quality': 60}, null=True, blank=True)
    pic5_description = models.CharField(max_length=500, default='Image Description', null=True, blank=True)
    pic6 = ProcessedImageField(upload_to="about_pic/icons/%y/%m/%d", processors=[ResizeToFill(42, 42)], format='png', options={'quality': 60}, null=True, blank=True)
    pic6_description = models.CharField(max_length=500, default='Image Description', null=True, blank=True)
    pic7 = ProcessedImageField(upload_to="about_pic/icons/%y/%m/%d", processors=[ResizeToFill(42, 42)], format='png', options={'quality': 60}, null=True, blank=True)
    pic7_description = models.CharField(max_length=500, default='Image Description', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return "Aboutus Icons"
    

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Aboutus icons'