from django.conf.urls import include, url
from cats_api.cats.models import Cat

from django.contrib import admin
admin.autodiscover()
admin.site.register(Cat)
urlpatterns = [
    url(r'^', include('cats_api.api.urls')),
    url(r'^admin/', admin.site.urls),
]