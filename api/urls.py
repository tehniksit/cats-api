from django.conf.urls import url, include
from cats_api.api import views
from cats_api.api.serializers import UserList, UserDetails
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers


#api_router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^api/cats/$', views.cats_list, name='cats_list'),
    url(r'^api/cat/(?P<pk>[0-9]+)$', views.cat_detail, name='cat_detail'),
    url('users/', UserList.as_view()),
    url('users/<pk>/', UserDetails.as_view()),
    
    
]