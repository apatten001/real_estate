from django.urls import path
from .views import HomeListView,HomeDetailView, ContactView,AboutView
app_name = 'houses'
urlpatterns = [
    path('home/', HomeListView.as_view(), name='list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('<int:pk>/', HomeDetailView.as_view(), name='detail'),

]