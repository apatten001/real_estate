from django.shortcuts import render
from .models import Author, NewsArticle
from django.urls import reverse_lazy, reverse
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, ListView, DetailView)
from rest_framework import viewsets

from .forms import ArticleForm
from .serializers import NewsArticleSerializer
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.

class NewsArticleViewset(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer


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
    paginate_by = 20

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


def article_form_view(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message='Article created')
            return redirect('news:article-list')
    else:
        form = ArticleForm()

    return render(request, 'news/article_form.html', {'form':form})



