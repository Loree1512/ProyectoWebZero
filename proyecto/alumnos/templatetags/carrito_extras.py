from django import template

register = template.Library()

def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''