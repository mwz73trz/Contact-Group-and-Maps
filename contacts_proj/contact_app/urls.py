from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('<int:contact_id>', views.contact_view, name='contact_view'),
    path('new', views.new_contact, name='new_contact'),
    path('edit/<int:contact_id>', views.edit_contact, name='edit_contact'),
    path('delete/<int:contact_id>', views.delete_contact, name='delete_contact'),
]