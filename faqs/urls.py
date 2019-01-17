from django.urls import path
from .views import FAQListView
app_name = 'faqs'

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faqs')


]