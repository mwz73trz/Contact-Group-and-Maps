from django.shortcuts import render, redirect
from django.forms import ModelForm
from contact_app.models import Contact

google_map_api_key = 'AIzaSyAObvwoFrF3tSU5HzknjAocZA0x67fQ6aI'

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

def create_modified_address(street, city, state):
    modified_address = street + ", " + city + " " + state
    google_address = modified_address.replace(' ', '%20')
    return f"https://www.google.com/maps/embed/v1/place?key=AIzaSyB97bf2HbQfZY0XuX-6XIKjI9Ho-Xjg18U&q={google_address}&zoom=18&maptype=satellite"

def contact_view(request, contact_id):
    contact = get_contact(contact_id)
    address_for_google = create_modified_address(contact.street, contact.city, contact.state)
    print(address_for_google)
    return render(request, 'contacts/contact_detail.html', {'contact': contact, 'map': address_for_google})

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



