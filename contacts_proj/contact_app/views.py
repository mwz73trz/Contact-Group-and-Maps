from django.shortcuts import render, redirect
from django.forms import ModelForm
from contact_app.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'street', 'city', 'state', 'zip', 'phone', 'email']

def get_contact(contact_id):
    return Contact.objects.get(id=contact_id)

def contact_list(request):
    contacts = Contact.objects.all()
    data = {'all_contacts': contacts}
    return render(request, 'contacts/contact_list.html', data)

def contact_view(request, contact_id):
    contact = get_contact(contact_id)
    data = {'contact': contact}
    return render(request, 'contacts/contact_detail.html', data)

def new_contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact_app:contact_list')
    return render(request, 'contacts/contact_form.html', {'form': form, 'new_or_edit': "New"})

def edit_contact(request, contact_id):
    contact = get_contact(contact_id)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contact_app:contact_list')
    return render(request, 'contacts/contact_form.html', {'form': form, 'new_or_edit': "Edit"})

def delete_contact(request, contact_id):
    contact = get_contact(contact_id)
    if request.method == "POST":
        contact.delete()
        return redirect('contact_app:contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'object': contact})



