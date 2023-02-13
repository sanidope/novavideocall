from django import forms
from . models import ContactFormModel

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactFormModel
        fields = ["email", "first_name", "last_name", "message"] 