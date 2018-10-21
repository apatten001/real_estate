from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import HomeListing
from news.models import Author, NewsArticle
from django.db.models.query import Q
from django.db.models import Avg, Max, Min
# Create your views here.


class HomeListView(ListView):

    '''
    Setting context data for our HomeList view.

    '''

    template_name = 'houses/index.html'

    def get_context_data(self,*args, **kwargs):
        context = super(HomeListView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        context['home'] = 'Your Home'
        context['jersey_homes'] = HomeListing.objects.filter(state__contains='nj')
        context['delaware_homes'] = HomeListing.objects.filter(state__contains='de',
                                                               zip_code__icontains=query == 19901)
        context['authors'] = Author.objects.filter(active=True)
        context['article'] = NewsArticle.objects.all()
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
        return HomeListing.objects.featured().order_by('-list_date')[:3]


class HomeDetailView(DetailView):

    queryset = HomeListing.objects.all()
