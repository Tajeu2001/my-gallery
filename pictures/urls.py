from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'pictures'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'search/', views.search_results, name='search'),
]    

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)