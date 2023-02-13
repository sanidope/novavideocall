from django.db import models
from django.contrib.auth.models import User 




class SecondColumn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_text = models.CharField(max_length=2000)
    second_text = models.CharField(max_length=2000)
    third_text = models.CharField(max_length=2000)
    fourth_text = models.CharField(max_length=2000)
 

    class Meta:
        verbose_name_plural = "SecondColumn"


class ThirdColumn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=2000)
    subtitle = models.CharField(max_length=2000)
    first_text = models.CharField(max_length=1000)
    second_text = models.CharField(max_length=1000)
    third_text = models.CharField(max_length=1000)
    fourth_text = models.CharField(max_length=1000)
    fifth_text = models.CharField(max_length=1000)
    sixth_text = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "ThirdColumn"



class FourthColumn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_text = models.CharField(max_length=1000)
    second_text = models.CharField(max_length=1000)
    third_text = models.CharField(max_length=1000)
    fourth_text = models.CharField(max_length=1000)
    fifth_text = models.CharField(max_length=1000)
    sixth_text = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "FourthColumn"


class FifthColumn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=2000)
    first_text = models.CharField(max_length=1000)
    second_text = models.CharField(max_length=1000)
    third_text = models.CharField(max_length=1000)


    class Meta:
        verbose_name_plural = "FifthColumn"


class SixthColumn(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    comment = models.CharField(max_length=100, null=True)
    fullname = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to="homepage/%y/%m/%d", null=True, blank=True)
    title = models.CharField(max_length=1000)
    first_text = models.CharField(max_length=1000)
    first_text_subtitle = models.CharField(max_length=1000, null=True)
    second_text = models.CharField(max_length=1000)
    second_text_subtitle = models.CharField(max_length=1000, null=True)
    third_text = models.CharField(max_length=1000)
    third_text_subtitle = models.CharField(max_length=1000, null=True)
    fourth_text = models.CharField(max_length=1000)
    fourth_text_subtitle = models.CharField(max_length=1000, null=True)

    class Meta:
        verbose_name_plural = "SixthColumn"
    
