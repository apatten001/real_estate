from django.shortcuts import render
from django.views.generic import ListView
from .models import  FrequentQuestionsAnswers
from .serializers import FAQSerializer

from rest_framework import viewsets


# Create your views here.


class FAQListView(ListView):

    model = FrequentQuestionsAnswers
    template_name = 'houses/faqs.html'

    paginate_by = 2


class FAQViewSet(viewsets.ModelViewSet):

    queryset = FrequentQuestionsAnswers.objects.all()
    serializer_class = FAQSerializer


