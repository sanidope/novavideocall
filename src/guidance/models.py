from django.db import models
from django.urls import reverse
from django.utils import timezone 
from tinymce.models import HTMLField
from django.contrib.auth.models import User 
# Create your models here.

class ItemBase(models.Model):
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug =  models.SlugField(max_length=250, unique_for_date='created')
    body = HTMLField()
    created = models.DateTimeField(default=timezone.now)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse("core:help_detail", args=[
            self.__class__.__name__.lower(),
            self.slug,
        ])
    
    
class Payment(ItemBase):

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Payments'
        
    

class MyAccounts(ItemBase):

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'MyAccounts'
        
    
class Purchasing(ItemBase):

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Purchasing'
        
    
class ProfilePlan(ItemBase):

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'ProfilePlan'
        

class Support(ItemBase):

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Support'
        
    

class More(ItemBase):

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'More'
        
