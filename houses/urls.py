from django.urls import path
from .views import HomeListView,HomeDetailView, AboutView
app_name = 'houses'
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('home/', HomeListView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('<int:pk>/', HomeDetailView.as_view(), name='detail'),

]