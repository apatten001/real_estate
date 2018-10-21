from django.shortcuts import render,Http404
from .models import Author,NewsArticle
from django.urls import reverse_lazy, reverse
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, ListView, DetailView)


# Create your views here.


class ArticleDetailView(DetailView):
    '''
    returns the detail of the article in the qs
    '''

    queryset = NewsArticle.objects.all()


class AuthorListView(ListView):
    '''
    Shows a list of all active authors
    '''
    context_object_name = 'author_list'
    paginate_by = 5

    queryset = Author.objects.all()


class ArticleListView(ListView):
    '''
    Returns a list of all articles in the database
    '''

    context_object_name = 'article_list'
    paginate_by = 5

    queryset = NewsArticle.objects.all().order_by('-timestamp')


class AuthorDetailView(DetailView):
    '''
    Gives detail about each Author with specific context
    related to the article category
    '''

    queryset = Author.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)

        context['news'] = NewsArticle.objects.filter()
        context['sports'] = NewsArticle.objects.filter()
        return context


class AuthorCreateView(CreateView):
    '''
    allows for creation for a new author
    '''

    model = Author
    success_url = reverse_lazy('news:author-list')
    fields = ['first_name', 'last_name']


class AuthorUpdateView(UpdateView):
    '''
    updates the authors information
    '''

    model = Author
    fields = ['first_name', 'last_name']


class AuthorDeleteView(DeleteView):
    '''
    ask for a deletion of an author
    '''

    model = Author
    success_url = reverse_lazy('author-list')

