"""Users URLs."""

# Django

from django.urls import path

from clinkmyhaus.apps.users.views import email_contact

app_name = 'users'

urlpatterns = [
    path('email-contact', email_contact, name='email_contact'),
]
