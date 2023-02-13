from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


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


