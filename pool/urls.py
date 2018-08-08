from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('domain_search', views.domain_search, name='domainSearch'),
    path('url_search', views.url_search, name='urlSearch'),
]
