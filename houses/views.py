from django.shortcuts import render, redirect
from django.db.models.query import Q
from django.db.models import Avg, Max, Min
from django.views.generic import ListView, DetailView, TemplateView

from .models import HomeListing
from .serializers import HomeListingSerializer
from news.models import Author, NewsArticle


from rest_framework import viewsets


class HomeListingViewSet(viewsets.ModelViewSet):

    """
    API for the HomeListing model
    """

    queryset = HomeListing.objects.all()
    serializer_class = HomeListingSerializer


class HomeListView(ListView):

    '''
    Setting context data for our HomeList view.

    '''

    template_name = 'houses/homelisting_list.html'

    def get_context_data(self,*args, **kwargs):
        context = super(HomeListView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        context['homes'] = HomeListing.objects.all()
        context['jersey_homes'] = HomeListing.objects.filter(state__contains='nj')
        context['delaware_homes'] = HomeListing.objects.filter(state__icontains='de')
        context['authors'] = Author.objects.filter(active=True)
        context['articles'] = NewsArticle.objects.all()
        num = HomeListing.objects.all().aggregate(Avg('cost'), Max('cost'), Min('cost'))
        context['avg_price'] = num.get('cost__avg')
        context['max_price'] = num.get('cost__max')
        context['min_price'] = num.get('cost__min')

        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')  # set default value after q None is default value
        if query is not None:
            lookups = (Q(city__icontains=query)|
                       Q(state__icontains=query)|
                       Q(zip_code__icontains=query)|
                       Q(address__icontains=query))
            return HomeListing.objects.filter(lookups).distinct()
        return HomeListing.objects.all().order_by('-img').distinct()


class HomeDetailView(DetailView):

    """
    Detail view of the HomeListing
    """

    queryset = HomeListing.objects.all()


class AboutView(TemplateView):

    """
    Render the template for the about page
    """

    template_name = 'houses/about.html'






