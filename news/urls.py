from django.urls import path
from .views import (AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
                    AuthorListView,ArticleDetailView,ArticleListView)

app_name = 'news'
urlpatterns = [
    path('author/', AuthorListView.as_view(), name='author-list'),
    path('article/', ArticleListView.as_view(), name='article-list'),
    path('author/<int:pk>/', ArticleDetailView.as_view(), name='author-detail'),
    path('author/add/', AuthorCreateView.as_view(), name='author-create')
]