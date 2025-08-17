from django import template
from django.contrib.auth.models import Group
from apps.posts.models import Post # Corrección en la importación

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()

@register.simple_tag
def get_recent_posts(count=5):
    """
    Retrieves a specified number of recent posts.
    """
    return Post.objects.filter(activo=True).order_by('-publicado')[:count]