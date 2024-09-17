from django.conf import settings
from django.contrib import admin
from django.contrib.admindocs.utils import docutils_is_available
from django.template.context_processors import static
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('video/', include('video.urls')),
    path ('admin/', admin.site.urls)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)