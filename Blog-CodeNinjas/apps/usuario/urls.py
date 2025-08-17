from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegistroView, CustomLoginView, logout_page

app_name = 'apps.usuario'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('registro/', RegistroView.as_view(), name='registrar'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('logout_page/', logout_page, name='logout_page')
]
