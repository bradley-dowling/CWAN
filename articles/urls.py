from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

################################################################
################################################################
## Name: urls.py
## Author: Bradley Dowling, 2021
## Description: urls.py defines the handling of URLs for the 
##              Articles app.
##
##

urlpatterns = [
    path('', views.home, name='home'),
    path('article_<int:article_id>', views.article_view, name='article_view'),
    path('volume_<int:volume_number>/', views.article_list, name='article_list'),
    path('download/article_<int:article_id>', views.article_download, name='article_download')
]