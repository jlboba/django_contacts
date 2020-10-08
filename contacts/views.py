from django.shortcuts import render, redirect

from .models import Contact 
from .forms import ContactForm

# Create your views here.

## index 
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', { 'contacts': contacts})

## show 
def contact_detail(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

## new 
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

## edit 
def contact_edit(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

## delete 
def contact_delete(request, pk):
    Contact.objects.get(id=pk).delete()
    return redirect('contact_list')
