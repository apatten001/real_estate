from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.


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