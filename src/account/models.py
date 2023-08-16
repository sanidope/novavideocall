from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.utils import timezone
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize


# Create your models here.
class Profile(models.Model):
    
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    
    user = models.OneToOneField(User,  related_name='userprofiles', on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='profile-pic/uploads/%y/%m/%d', default='avatar.png')
    smart = ImageSpecField(source='profile_pic', processors=[SmartResize(512,512)]) 
    gender = models.CharField(max_length=50, choices=GENDER, blank=True, null=True)
    profile_updated = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return "{} Profile".format(self.user)


    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Profile'



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

                
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
