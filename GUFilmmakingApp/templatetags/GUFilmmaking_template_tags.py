from django import template
from GUFilmmakingApp.models import Post

register = template.Library()

@register.simple_tag
def get_most_viewed_posts(count=3):
    return Post.objects.order_by('-views')[:count]
