from django.contrib import admin
from .models import Post, Comentario, Categoria

# Clase de administración para el modelo Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Esto le dice a Django que el campo 'slug' se debe rellenar automáticamente
    # usando el contenido del campo 'nombre'.
    prepopulated_fields = {'slug': ('nombre',)}

# Clase de administración para el modelo Post (opcional, pero buena práctica)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'publicado', 'categoria']
    list_filter = ['publicado', 'categoria']
    search_fields = ['titulo', 'subtitulo']
    
# Clase de administración para el modelo Comentario (opcional)
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['autor', 'post', 'fecha_creacion', 'aprobado']
    list_filter = ['aprobado', 'fecha_creacion']
    search_fields = ['autor__username', 'contenido']