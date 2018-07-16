from django.conf.urls import include, url
from cats_api.cats.models import Cat
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
admin.site.register(Cat)
urlpatterns = [
    url(r'^', include('cats_api.api.urls')),
    url(r'^admin/', admin.site.urls),
    url('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
