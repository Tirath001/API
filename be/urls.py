from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from website import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('api/auth/', include('auth_app.urls')),
    path('jobs/', include('jobportal.urls')),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)