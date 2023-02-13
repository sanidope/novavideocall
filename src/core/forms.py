from django import forms
from .models import  SubscribeNewsletter


class LizzyForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    class Meta:
        fields = ('email',)
        
        
        
        
class NadiaForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    class Meta:
        fields = ('email',)


class SubscribeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = SubscribeNewsletter
        fields = ('email',)
