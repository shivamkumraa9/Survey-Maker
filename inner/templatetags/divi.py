from django import template

register = template.Library()

@register.filter()
def divide(value, arg):
    """Removes all values of arg from the given string"""
    try:
    	val = (value//arg)*100
    	return val
    except:
    	return 0
