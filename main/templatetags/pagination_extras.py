from django import template

register = template.Library()

@register.filter
def get_range(value):
    """Returns a range for pagination controls."""
    return range(1, value+1)
