from django import forms
from .models import  (
    NadiaClients,
    LizzyClients,
    ZaaloloClients,
    KingpindrakoClients,
    SubscribeNewsletter,
)


class LizzyForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    class Meta:
        fields = ('email',)
        model = LizzyClients
        
        
        
        
class NadiaForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    class Meta:
        fields = ('email',)
        models = NadiaClients


class ZaaloloForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    class Meta:
        fields = ('email',)
        model = ZaaloloClients


class KingpindrakoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    class Meta:
        fields = ('email',)
        model = KingpindrakoClients


class SubscribeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = SubscribeNewsletter
        fields = ('email',)
