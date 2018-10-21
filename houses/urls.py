from django.urls import path
from .views import HomeListView,HomeDetailView
app_name = 'houses'
urlpatterns = [
    path('', HomeListView.as_view(), name='list'),
    path('<int:pk>/', HomeDetailView.as_view(), name='detail'),

]