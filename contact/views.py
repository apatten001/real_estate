from django.shortcuts import render, redirect
from .forms import ContactForm
from .serializers import ContactSerializer
from .models import Contact

from rest_framework import viewsets
# Create your views here.


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


def add_contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('houses:home')
    else:
        form = ContactForm()
        return render(request, 'houses/contact.html', {'form': form})