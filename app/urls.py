from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.index, name='index'),
   path('movies', views.movielist, name='movielist'),
   path('search_results', views.search_results, name='search_results')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)