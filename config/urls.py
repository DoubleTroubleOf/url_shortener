from django.contrib import admin
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from shortener.views import UrlsListViewSet, UrlShortener, UrlExport, UrlView

router = DefaultRouter()
router.register('', UrlsListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^shortener/(?P<origin_url>.+)$', UrlShortener.as_view()),
    path('export/', UrlExport.as_view()),
    re_path(r'^(?P<hash>.+)$', UrlView.as_view()),
]

urlpatterns += router.urls