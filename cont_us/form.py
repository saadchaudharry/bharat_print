from django import forms
from .models import ContactUs


class ContactUS_form(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name",'email','phone','msG']