from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('new', views.new_subject, name='new_subject'),
    path('<int:subject_id>', views.subject_detail, name='subject_detail'),
    path('<int:subject_id>/edit', views.edit_subject, name='edit_subject'),
    path('<int:subject_id>/delete', views.delete_subject, name='delete_subject'),
    path('<int:subject_id>/contacts', views.contact_list, name='contact_list'),
     path('<int:subject_id>/contacts/new', views.new_contact, name='new_contact'),
    path('<int:subject_id>/contacts/<int:contact_id>', views.contact_view, name='contact_view'),
    path('<int:subject_id>/contacts/<int:contact_id>/edit', views.edit_contact, name='edit_contact'),
    path('<int:subject_id>/contacts/<int:contact_id>/delete', views.delete_contact, name='delete_contact'),
]