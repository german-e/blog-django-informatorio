from django.urls import path
from .views import ContactoCreateView, enviar_mensaje

app_name = 'apps.contacto'

urlpatterns = [
    path('', ContactoCreateView.as_view(), name='contacto'),
    path('enviar-mensaje/', enviar_mensaje, name='enviar_mensaje'),
]