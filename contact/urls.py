from django.urls import path
from .views import add_contact

app_name = 'contact'

urlpatterns = [
    path('contact/', add_contact, name='add-contact'),




]

