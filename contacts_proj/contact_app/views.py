from django.shortcuts import render, redirect
from django.forms import ModelForm
from contact_app.models import Contact, Subject
from .forms import ContactForm, SubjectForm
from django.contrib.auth.decorators import login_required

google_map_api_key = 'AIzaSyAObvwoFrF3tSU5HzknjAocZA0x67fQ6aI'

def get_subject(subject_id):
    return Subject.objects.get(id=subject_id)

@login_required
def subject_list(request):
    subjects = Subject.objects.filter(user=request.user)
    return render(request, 'subjects/subject_list.html', {'subjects': subjects})

def subject_detail(request, subject_id):
    subject = get_subject(subject_id)
    return render(request, 'subjects/subject_detail.html', {'subject': subject})

def new_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            return redirect('contact_app:subject_detail', subject_id=subject.id)
    else:
        form = SubjectForm()
    return render(request, 'subjects/subject_form.html', {'form': form, 'type_of_request': 'New'})

def edit_subject(request, subject_id):
    subject = get_subject(subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            return redirect('contact_app:subject_detail', subject_id=subject.id)
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subjects/subject_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_subject(request, subject_id):
    subject = get_subject(subject_id)
    if request.method == "POST":
        subject.delete()
        return redirect('contact_app:subject_list')
    return render(request, 'subjects/subject_confirm_delete.html', {'object': subject})

def get_contact(contact_id):
    return Contact.objects.get(id=contact_id)

def contact_list(request, subject_id):
    subject = get_subject(subject_id)
    contacts = subject.contacts.all()
    return render(request, 'contacts/contact_list.html', {'subject': subject, 'contacts': contacts})

def create_modified_address(street, city, state):
    modified_address = street + ", " + city + " " + state
    google_address = modified_address.replace(' ', '%20')
    return f"https://www.google.com/maps/embed/v1/place?key=AIzaSyB97bf2HbQfZY0XuX-6XIKjI9Ho-Xjg18U&q={google_address}&zoom=18&maptype=satellite"

def contact_view(request, subject_id, contact_id):
    subject = get_subject(subject_id)
    contact = get_contact(contact_id)
    address_for_google = create_modified_address(contact.street, contact.city, contact.state)
    print(address_for_google)
    return render(request, 'contacts/contact_detail.html', {'subject': subject, 'contact': contact, 'map': address_for_google})

def new_contact(request, subject_id):
    subject = get_subject(subject_id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.subject = subject
            contact.save()
            return redirect('contact_app:contact_view', subject_id=contact.subject.id, contact_id=contact.id)
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form, 'type_of_request': "New"})

def edit_contact(request, subject_id, contact_id):
    subject = get_subject(subject_id)
    contact = get_contact(contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contact_app:contact_view', subject_id=subject.id, contact_id=contact.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form, 'type_of_request': "Edit"})

def delete_contact(request, subject_id, contact_id):
    contact = get_contact(contact_id)
    if request.method == "POST":
        contact.delete()
        return redirect('contact_app:contact_list', subject_id=subject_id)
    return render(request, 'contacts/contact_confirm_delete.html', {'object': contact})



