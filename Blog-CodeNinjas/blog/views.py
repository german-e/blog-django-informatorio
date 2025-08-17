# blog/views.py

from django.shortcuts import render
from apps.posts.models import Post, Categoria # Importa el modelo Categoria

def index(request):
    latest_posts = Post.objects.all().order_by('-publicado')[:3]
    categorias = Categoria.objects.all() # Obtiene todas las categorías
    context = {
        'latest_posts': latest_posts,
        'categorias': categorias, # Agrega las categorías al contexto
    }
    return render(request, 'index.html', context)

def acerca_de(request):
    return render(request, 'acerca/acerca.html') # Corregido para que apunte a 'acerca.html'
