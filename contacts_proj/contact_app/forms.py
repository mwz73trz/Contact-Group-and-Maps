from django import forms
from django.forms.models import ModelForm
from .models import Contact, Subject

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'description', 'created_on', 'user']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'street', 'city', 'state', 'zip', 'phone', 'email', 'subject']