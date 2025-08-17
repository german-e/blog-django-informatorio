# blog/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('posts/', include('apps.posts.urls')),
    path('contacto/', include('apps.contacto.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('acerca/', include('apps.acerca.urls')), # <--- Agrega o cambia esta línea
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
