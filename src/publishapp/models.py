from django.db import models
from django.urls import reverse
from django.utils import timezone 
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Posts(models.Model):
    tags = TaggableManager()
    objects = models.Manager()
    published = PublishedManager() 
    
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug =  models.SlugField(max_length=250, unique_for_date='publish')
    body = HTMLField()
    post_image = models.ImageField(upload_to="Blog/images/%y/%m/%d", blank=True, null=True)
    post_image_description = models.CharField(max_length=500, default='Image Description')
    post_image_small = ImageSpecField(source='post_image', processors=[ResizeToFill(209, 173)], format='JPEG', options={'quality': 60})
    post_image_large = ImageSpecField(source='post_image', processors=[ResizeToFill(926, 520)], format='JPEG', options={'quality': 60})
    post_image_related = ImageSpecField(source='post_image', processors=[ResizeToFill(356, 295)], format='JPEG', options={'quality': 60})
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    @property
    def convert_in_meta(self):
        title = (self.title)[0:50]
        body = (self.body)[0:100]
        description = title + str(body)
        return description


    @property
    def convert_title_in_meta(self):
        title = (self.title)[0:50]
        return title

    
    class Meta:
        ordering = ('-publish',)
        verbose_name_plural = 'Posts'
        
    def __str__(self):
        return self.title 
    
    
    def get_absolute_url(self):
        return reverse("publishapp:post_detail", args=[
            self.slug
        ])
    

class AboutAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    author_pic_description = models.CharField(max_length=500, default='Image Description')
    author_pic = ProcessedImageField(upload_to="AboutAuthor/%y/%m/%d", processors=[ResizeToFill(90, 90)],  format='JPEG', options={'quality': 60} )
    description = HTMLField()


    def __str__(self):
        return "About Author"

    class Meta:
        verbose_name_plural = 'About Author'