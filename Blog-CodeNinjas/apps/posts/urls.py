from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    CrearPostView, 
    PostUpdateView, 
    PostDeleteView,
    ComentarioUpdateView,
    ComentarioDeleteView,
    PostSearchView,
     DarLikeAjaxView, # Agrega esta importación
)

app_name = 'apps.posts'

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('busqueda/', PostSearchView.as_view(), name='busqueda'), # Agrega esta línea
    path('<int:pk>/', PostDetailView.as_view(), name='post_individual'),
    path('crear/', CrearPostView.as_view(), name='crear_post'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('<int:pk>/eliminar/', PostDeleteView.as_view(), name='eliminar_post'),
    path('comentario/<int:pk>/editar/', ComentarioUpdateView.as_view(), name='editar_comentario'),
    path('comentario/<int:pk>/eliminar/', ComentarioDeleteView.as_view(), name='eliminar_comentario'),
    path('<int:pk>/like/', DarLikeAjaxView.as_view(), name='dar_like'),
]