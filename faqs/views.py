from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from rest_framework import viewsets

from contact.forms import SubscribeForm
from .models import FrequentQuestionsAnswers
from .serializers import FAQSerializer


# Create your views here.


class FAQListView(FormMixin, ListView):

    form_class = SubscribeForm
    model = FrequentQuestionsAnswers
    template_name = 'houses/faqs.html'

    paginate_by = 2


def add_subscriber(request):

    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscribe = form.save()
            subscribe.save()
            return redirect('houses:home')
    else:
        form = SubscribeForm()
        return render(request, 'houses/faqs.html', {'form': form})


class FAQViewSet(viewsets.ModelViewSet):

    queryset = FrequentQuestionsAnswers.objects.all()
    serializer_class = FAQSerializer


