"""real_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from users.views import register
from rest_framework import routers
from faqs.views import FAQViewSet
from houses.views import HomeListingViewSet
from contact.views import ContactViewSet
from news.views import NewsArticleViewset


router = routers.DefaultRouter()

router.register(r'faqs', FAQViewSet)
router.register(r'houses', HomeListingViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'news', NewsArticleViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('api/v1/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('houses.urls')),
    path('', include('news.urls')),
    path('', include('contact.urls')),
    path('', include('faqs.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
