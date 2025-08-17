from django.urls import path
from . import views

app_name = 'acerca'

urlpatterns = [
    path('', views.acerca_de, name='acerca_de'),
]
