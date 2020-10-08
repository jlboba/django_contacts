from django import forms 
from .models import Contact 

class ContactForm(forms.modelForm):
    class Meta:
        model = Contact 
        fields = ('name', 'age',)