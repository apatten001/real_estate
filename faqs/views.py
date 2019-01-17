from django.shortcuts import render
from django.views.generic import ListView
from .models import  FrequentQuestionsAnswers
# Create your views here.


class FAQListView(ListView):

    model = FrequentQuestionsAnswers
    template_name = 'houses/faqs.html'

    paginate_by = 2

