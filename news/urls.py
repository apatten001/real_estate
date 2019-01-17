from django.urls import path
from .views import (AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
                    AuthorListView,ArticleDetailView,ArticleListView,article_form_view)

app_name = 'news'
urlpatterns = [
    path('author/', AuthorListView.as_view(), name='author-list'),
    path('article/', ArticleListView.as_view(), name='article-list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('article-form/', article_form_view, name='article-form'),
    path('author/<int:pk>/', ArticleDetailView.as_view(), name='author-detail'),
    path('author/add/', AuthorCreateView.as_view(), name='author-create')
]