from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'bio', 'liveImage', 'album1', 'image1', 'album2', 'image2', 'link')
