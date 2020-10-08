from django.shortcuts import render

from .models import Contact 

# Create your views here.

## index 
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', { 'contacts': contacts})

## show 
def contact_detail(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})