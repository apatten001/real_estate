from django.db.models import Avg, Max, Min
from django.db.models.query import Q
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from rest_framework import viewsets

from news.models import Author, NewsArticle
from .models import HomeListing
from .serializers import HomeListingSerializer


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

    template_name = ['houses/homelisting_list.html', 'houses/footer.html']
    paginate_by = 8

    def get_context_data(self,*args, **kwargs):
        context = super(HomeListView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        context['homes'] = HomeListing.objects.all()
        context['jersey_homes'] = HomeListing.objects.filter(state__contains='nj')
        context['delaware_homes'] = HomeListing.objects.filter(state__icontains='de')
        context['authors'] = Author.objects.filter(active=True)
        context['articles'] = NewsArticle.objects.all()
        context['recent_articles'] = NewsArticle.objects.all()[:3]
        context['count'] = HomeListing.objects.all().count()

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






