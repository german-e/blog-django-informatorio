from django.db import models
from django.utils import timezone
from django.conf import settings
from apps.usuario.models import Usuario

# Categoria (entidad)
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.nombre

# --- Función para obtener la categoría por defecto ---
def get_categoria_sin_categoria():
    return Categoria.objects.get_or_create(nombre='Sin categoria', slug='sin-categoria')[0] # Agregamos slug para evitar errores

# Post (entidad)
class Post(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    subtitulo = models.CharField(max_length=200, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default=get_categoria_sin_categoria)
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(Usuario, related_name='likes', blank=True, null=True)

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo

    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()

    def total_likes(self):
        return self.likes.count()

    def le_dio_like(self, user):
        return self.likes.filter(pk=user.pk).exists()

# Comentario
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=True)
    class Meta:
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'Comentario de {self.autor.username} en "{self.post.titulo}"'