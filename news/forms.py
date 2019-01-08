from django import forms

from .models import NewsArticle


class ArticleForm(forms.ModelForm):

    class Meta:
        model = NewsArticle
        fields = ['author', 'Title', 'content']

