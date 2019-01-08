from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('news:author-detail', kwargs={'pk': self.pk})

    def full_name(self):
        return self.first_name + " " + self.last_name


class NewsArticle(models.Model):

    Title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author,  on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title




