from django import template

register = template.Library()


@register.filter
def dictvalue(dict, key):
    return dict.get(key)
