from django.conf.urls import url, include
from cats_api.api import views

urlpatterns = [
    url(r'^api/cats/$', views.cats_list, name='cats_list'),
    url(r'^api/cat/(?P<pk>[0-9]+)$', views.cat_detail, name='cat_detail'),
]